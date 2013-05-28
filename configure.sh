#!/bin/bash
### THE NAME OF BUILD DIR IS NEW CONSTRAINT.
### IT SOULD BE CALLED build


if [ ! -d "./sip2ser" ]; then
    #we aren't in src_dir take right action
    if [ -d "./patchs" ]; then
	#we are in sip2ser tree
	cd ..
    else
	#we probably are in build dir
	echo "Warn we can't be sure on where we are. if you are in your build dir that's ok"
	cd ..
    fi
fi

if [ ! -d "./build" ]; then
    mkdir build
fi

src_dir=`pwd`
build_dir=$src_dir"/build"
sip2ser_dir=$src_dir"/sip2ser"
stdconfigure=$src_dir"/configure"


sed -e "s,@SRC_DIR\@,$src_dir,g"   \
    -e "s,@BUILD_DIR\@,$build_dir,g"   \
    -e "s,@FASTDATATEL_DIR\@,$sip2ser_dir,g" \
    $sip2ser_dir/Rakefile.in > $build_dir/Rakefile

#ln -s $sip2ser_dir/tests $build_dir

echo -ne "ruby and rake are necessary "

system_rake=`whereis rake | awk '{ print $2}'`
system_ruby=`whereis ruby | awk '{ print $2}'`
system_wget=`whereis wget | awk '{ print $2}'`
epel_pkg="epel-release-6-8.noarch.rpm"

echo  "setting up some environments ...."

LIBS=$sip2ser_dir/libs/*

if [ "$(ls -A `dirname $LIBS[0]`)" ]; then
    for f in $LIBS
    do
	dest=$(basename $f)
	if [[ ! -e $src_dir/$dest ]]; then
	    echo "Processing $f folder..."
	    ln -s $f $src_dir/$dest
	fi
    done
fi

echo -ne "checking for  availability .....\t\t"

if [[ ! -f $system_rake || ! -f $system_ruby ]]; then
    echo "FAIL"
    echo "some within rake or ruby are missied on you system do you want install?[y/*]"
    read choose
    if [ $choose=="y" ]; then
	echo "installing ...."
	sudo yum install -y ruby rubygem-rake
    else
	echo "your choose -> $choose <- is considered as no"
	echo "please install ruby and rubygem-rake manually"
    fi
else
    echo "OK"
fi

if [[ ! -f $system_wget ]]; then
    sudo yum install -y wget
else
    echo "wget found"
fi

echo -ne "autoreconf needed, check for availability .....\t\t"

reconfig_command=`whereis autoreconf | awk '{ print $2}'`

if [[ -f $reconfig_command && ! -z $reconfig_command ]]; then
    echo "OK"
    $reconfig_command -if
else
    echo "FAIL"
    echo "autoreconf command is missied on you system do you want install?[y/*]"
    read choose
    if [ $choose=="y" ]; then
        echo "installing ...."
        sudo yum install -y autoconf automake
    else
        echo "your choose -> $choose <- is considered as no"
	echo "autoreconf missing: remember to run prereq task and then rerun autoreconfig -if"
    fi
fi

cd ..
# we need to add support for go stuff
GROOT=`pwd`

if [ "$GOROOT"=="" ]; then
    wget https://go.googlecode.com/files/go1.1.src.tar.gz
    tar xzpvf go1.1.src.tar.gz
    cd go/src
    ./all.bash
    goroot=`cat ~/.bash_profile | grep GOROOT`
    if [ $goroot=="" ]; then
	echo "GOROOT=$GROOT/go" >> ~/.bash_profile
	echo "export GOROOT" >> ~/.bash_profile
	echo "PATH=$PATH:$GOROOT/bin" >> ~/.bash_profile
	echo "export PATH" >> ~/.bash_profile
    fi
fi

# if on centos we need to install epel
if [[ -f /etc/redhat-release ]]; then
distro=`cat /etc/redhat-release | awk '{ print $1 }'`
version=` cat /etc/redhat-release | awk '{ print $3 }'`
if [[ "$distro" -eq "CentOS" ]]; then
    if [[ $version == 6* ]]; then
	if [[ ! -f $epel_pkg ]]; then
	    wget http://mirror.switch.ch/ftp/mirror/epel/6/x86_64/$epel_pkg
	fi
	sudo yum localinstall $epel_pkg
	echo "would you like to add custom sip2ser repo?[y/*]"
	read rchoose
	if [ $rchoose=="y" ]; then
	    sudo wget http://192.168.64.35/opsip4.6-unstable-centos6.repo -P /etc/yum.repos.d/
	else
	    echo "your choose -> $rchoose <- is considered as no-> we are not adding sip2ser repo"
	fi
	    
    fi
fi
fi

GIT_DIR=$src_dir/.git
GUILT_DIR=$GIT_DIR/patches
[ ! -d "$GUILT_DIR" ] && ln -s "$sip2ser_dir/patches" "$GUILT_DIR"
mkdir -p "$GUILT_DIR/$branch"
touch "$GUILT_DIR/$branch/series"
touch "$GUILT_DIR/$branch/status"

mkdir -p "$GIT_DIR/hooks/guilt"
cat > "$GIT_DIR/hooks/guilt/delete" <<EOF
#!/bin/sh
# Usage: <script> <patch being removed>

echo "Removing patch '\$1'..."
EOF

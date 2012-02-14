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
	echo "Warn we can't be sure on where we are. if you are in your build dir all ok"
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

ln -s $sip2ser_dir/tests $build_dir

echo -ne "ruby and rake are necessary "

system_rake=`whereis rake | awk '{ print $2}'`
system_ruby=`whereis ruby | awk '{ print $2}'`

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

echo -ne "autoreconf needed, check for availability .....\t\t"

reconfig_command=`whereis autoreconf | awk '{ print $2}'`
    
if [[ -f $reconfig_command && ! -z $reconfig_command ]]; then
    echo "OK"
    $reconfig_command -if
else
    echo "FAIL"
    echo "autoreconf missing: remember to run prereq task and then rerun autoreconfig -if"
fi

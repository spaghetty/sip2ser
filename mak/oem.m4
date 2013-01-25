define(`sipx_packages',
sipx_packages()
s2s
)
define(`welcome_message',
 
Welcome to s2s
=============================
First time logon: user = root     password = setup
 
)
define(`repo_contents',
[s2s]
name=s2s CentOS \$releasever - \$basearch
baseurl=http://192.168.64.35/unstable_repo/PACKAGE_VERSION()/CentOS_\$releasever/
enabled=1
gpgcheck=0
)
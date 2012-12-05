define(`sipx_packages',
sipx_packages()
ezuce
)
define(`welcome_message',
 
Welcome to eZuce
=============================
First time logon: user = root     password = setup
 
)
define(`repo_contents',
[ezuce]
name=ezuce CentOS \$releasever - \$basearch
baseurl=http://download.example.com/ezuce/PACKAGE_VERSION()/CentOS_\$releasever/
enabled=1
gpgcheck=0
)
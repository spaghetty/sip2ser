%post
#chkconfig sipxecs off
echo "%wheel  ALL=(ALL)   ALL" >> /etc/sudoers

#create custome firstboot
#mv /usr/sbin/firstboot /usr/sbin/firstboot-old
#ln -s /usr/bin/opsip-setup-system /usr/sbin/firstboot

#chkconfig NetworkManager off

sed 's:127\.0\.0\.1.*:127\.0\.0\.1	localhost.localdomain	localhost:' /etc/hosts > /etc/hosts

echo "#!/bin/bash"  > /etc/init.d/unicode
echo "# unicode	    Starts unicode support." >> /etc/init.d/unicode
echo "# chkconfig:  2345 50 88 " >> /etc/init.d/unicode
echo "" >> /etc/init.d/unicode
echo "unicode_start" >> /etc/init.d/unicode
chmod 777 /etc/init.d/unicode
chkconfig unicode on

echo "#!/bin/bash"  > /etc/init.d/udisks
echo "# udisks	    Starts udisks daemon." >> /etc/init.d/udisks
echo "# chkconfig:  23 50 90 " >> /etc/init.d/udisks
echo "" >> /etc/init.d/udisks
echo "/usr/libexec/udisks-daemon &> /var/log/udisk-daemon &"  >> /etc/init.d/udisks
chmod 777 /etc/init.d/udisks
chkconfig udisks on

#creazione archivio
tar czpvf /usr/local/image/system_backup.tar.gz -C / bin boot cgroup etc home lib lib64 media opt root sbin selinux srv usr var


#... Setup initial setup script to run one time (after initial reboot only)
cat >> /root/.bashrc <<EOF

/usr/bin/sipxecs-setup
# restore /root/.bashrc and /etc/issue to original states upon successful
# setup.
if [ \$? == 0 ]; then
  sed -i '/^\/usr\/bin\/sipxecs-setup\$/,//d' /root/.bashrc
  sed -i '/^====/,//d' /etc/issue
fi
EOF

# the script removes itself from the root .bashrc file when it completes

#... Add logon message
cat >> /etc/issue <<EOF

==========================
Welcome to SIPfoundry sipXecs.

After logging in as root you will automatically be taken through a setup
procedure.

EOF

cat > /etc/yum.repos.d/sipxecs.repo <<EOF
[sipXecs]
name=sipXecs for CentOS - \$basearch
baseurl=http://download.sipfoundry.org/pub/sipXecs/4.6.0/CentOS_6/\$basearch
enabled=1
gpgcheck=0

EOF

#... Boot kernel in quiet mode
sed -i 's/ro root/ro quiet root/g' /boot/grub/grub.conf

# Turn off unused services that listen on ports
chkconfig portmap off
chkconfig netfs off
chkconfig nfslock off

eject



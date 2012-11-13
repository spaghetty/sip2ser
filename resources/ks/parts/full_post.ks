%post
chkconfig sipxecs off
echo "%wheel  ALL=(ALL)   ALL" >> /etc/sudoers

#create custome firstboot
mv /usr/sbin/firstboot /usr/sbin/firstboot-old
ln -s /usr/bin/opsip-setup-system /usr/sbin/firstboot

chkconfig NetworkManager off

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
chmod 644 /usr/bin/sipxecs-setup-system


#creazione archivio
tar czpvf /usr/local/image/system_backup.tar.gz -C / bin boot cgroup etc home lib lib64 media opt root sbin selinux srv usr var

%end

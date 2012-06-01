# Kickstart file for composing the "Fedora" spin of Fedora (rawhide)
# Maintained by the Fedora Release Engineering team:
# https://fedoraproject.org/wiki/ReleaseEngineering
# mailto:rel-eng@lists.fedoraproject.org

# Use a part of 'iso' to define how large you want your isos.
# Only used when composing to more than one iso.
# Default is 695 (megs), CD size.
# Listed below is the size of a DVD if you wanted to split higher.
#part iso --size=4998

# Add the repos you wish to use to compose here.  At least one of them needs group data.
repo --name=fedora --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=fedora-14&arch=x86_64
#repo --name=fedora-source  --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=fedora-source-14&arch=x86_64
repo --name="Opsip" --baseurl="http://192.168.64.35/unstable_repo/Fedora_14/x86_64/" --noverifyssl
repo --name="Opsip-source" --baseurl="http://192.168.64.35/unstable_repo/Fedora_14/source/" --noverifyssl

install
lang en_US.UTF8
keyboard us
timezone --utc Europe/Rome
rootpw --plaintext sip2ser123
# Disk partitioning information
clearpart --all
zerombr
part / --asprimary --fstype="ext4" --size=20000
part /var --fstype="ext4" --size=20000
part swap --fstype="swap" --size=6000
part /usr/local/image --fstype="ext4" --grow --size=1

authconfig  --useshadow  --passalgo=sha512

bootloader --location=mbr --driveorder=sda --timeout=3

firewall --disabled
selinux --disabled

text

user --name="admin" --groups="wheel,wireshark" --password="sip2ser" --plaintext

firstboot --enable

halt

network --bootproto=dhcp

# Package manifest for the compose.  Uses repo group metadata to translate groups.
# (@base is added by default unless you add --nobase to %packages)
# (default groups for the configured repos are added by --default)
%packages
@admin-tools
@base
@core
@X Window System
@GNOME Desktop Environment
wireshark-gnome	
telnet
emacs
firefox
dhcp
s2sopsip
s2sctilink
s2scdrextractor
s2srecorder
s2sfaxspool
s2sivr
conferencereservation
ivrgui
getmail
ssmtp
%end

%post
chkconfig sipxecs off
echo "%wheel  ALL=(ALL)   ALL" >> /etc/sudoers

#create custome firstboot
mv /usr/sbin/firstboot /usr/sbin/firstboot-old
ln -s /usr/bin/opsip-setup-system /usr/sbin/firstboot

#creazione archivio
tar czpvf /mnt/sysimage/usr/local/image/system_backpu.tar.gz --exclude="/mnt/sysimage/lost+found/*" --exclude="/mnt/sysimage/usr/local/image/*" --exclude="/mnt/sysimage/proc/*" --exclude="/mnt/sysimage/sys/*" -C /mnt/sysimage/ *


%end
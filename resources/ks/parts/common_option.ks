text
install
cdrom
reboot
lang en_US.UTF-8
keyboard us
timezone --utc Europe/Rome
rootpw --plaintext sip2ser123

authconfig  --useshadow  --passalgo=sha512

bootloader --location=mbr --driveorder=sda --timeout=3

#firewall --disabled
#selinux --disabled

user --name="admin" --groups="wheel,wireshark" --password="sip2ser" --plaintext

#firstboot --enable

#halt

network --bootproto=dhcp


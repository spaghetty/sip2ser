clearpart --all
zerombr
part / --asprimary --fstype="ext4" --size=10000
part /var --fstype="ext4" --size=20000
part swap --fstype="swap" --size=6000
part /usr/local/image --fstype="ext4" --grow --size=1

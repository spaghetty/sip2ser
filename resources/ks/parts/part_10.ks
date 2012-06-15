# Disk partitioning information
clearpart --all
zerombr
part / --asprimary --fstype="ext4" --size=5000
part swap --fstype="swap" --size=600
part /usr/local/image --fstype="ext4" --grow --size=1

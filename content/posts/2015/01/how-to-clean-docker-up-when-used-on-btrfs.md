+++
title = "How to clean docker up when used on btrfs"
date = 2015-01-08T13:05:16+00:00
+++
My docker uses to forget a lot of files when I just remove the images with `rmi`.

```
systemctl stop docker.service
systemctl stop docker.socket
rm -rf /var/lib/docker/
btrfs subvolume list /var/lib/docker|awk '/ID/ {print "/"$9}'|xargs btrfs sub delete
```

+++
title = "How to clean Docker up when used on Btrfs"
date = 2015-01-08T13:05:16+00:00
[taxonomies]
tags = ["tips", "linux", "containers"]
+++
Docker often leaves behind files when I remove images with `rmi`.

```
systemctl stop docker.service
systemctl stop docker.socket
rm -rf /var/lib/docker/
btrfs subvolume list /var/lib/docker|awk '/ID/ {print "/"$9}'|xargs btrfs sub delete
```

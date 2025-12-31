+++
title = "Prefetch apt packages"
date = 2012-11-13T10:26:46+00:00
+++
I use this command to speed up deb package downloads. It will do parallel downloads of the required .deb files with puf.

For example with otrs:

```shell
cd /var/cache/apt/archives/ && apt-get -y --print-uris install otrs|awk '{print $1}'|grep "'http" | xargs puf
```

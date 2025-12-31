+++
title = "prefetch apt packages"
date = 2012-11-13T10:26:46+00:00
+++
I use this command to speed up deb packages download. It will do parallel download of the require .deb files with puf.

For example with otrs:`cd /var/cache/apt/archives/ && apt-get -y --print-uris install otrs|awk '{print $1}'|grep "'http" | xargs puf`

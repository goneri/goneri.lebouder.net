+++
title = "Pbuilder on Debian kFreeBSD Wheezy"
date = 2014-10-06T19:57:17+00:00
[taxonomies]
tags = ["tips", "bsd", "debian"]
+++
There is a little trick if you want to use pbuilder on kFreeBSD. Add these lines in /etc/pbuilderrc:

```
MIRRORSITE=http://cdn.debian.net/debian
USEPROC=yes
USEDEVFS=yes
USEDEVPTS=yes
BINDMOUNTS="/home/goneri"
```

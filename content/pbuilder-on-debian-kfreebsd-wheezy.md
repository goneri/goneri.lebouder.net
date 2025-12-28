+++
title = "pbuilder on Debian kFreeBSD Wheezy"
date = 2014-10-06T19:57:17+00:00
+++
There is a little trick if you want to use pbuilder on kFreeBSD. Add these links in /etc/pbuilderrc:
> MIRRORSITE=http://cdn.debian.net/debian**USEPROC=yes****USEDEVFS=yes****USEDEVPTS=yes**BINDMOUNTS="/home/goneri"

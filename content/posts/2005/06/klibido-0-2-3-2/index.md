+++
title = "klibido 0.2.3-2"
date = 2005-06-25T00:48:00+00:00
+++

![klibido-128-2.png](klibido-128-2.png)

I've just finish to update the [klibido](http://klibido.sf.net/) package for Debian. For the moment, it can't be upload in the official repository before the end of the [gcc4 ABI transition](http://lists.debian.org/debian-devel-announce/2005/06/msg00004.html). The majors changes are the inclusion of Bauno's "Please subscribe me!" patch and another patch from Loïc Pefferkorn.

Loïc Pefferkorn decided to package klibido for Ubuntu, since this distribution is based on Debian he asked me for working together. Welcome Loïc !
Tonight i add a patch from him to move the "klibido.desktop" file to a more common place. Thanks ;).

To install klibido on you Debian, please add this lines on your /etc/apt/sources.list file.

> deb http://orniere-du-globe.net/debian ./
> deb-src http://orniere-du-globe.net/debian ./

Than you have just to update the index and install it.

> apt-get update
> apt-get install klibido
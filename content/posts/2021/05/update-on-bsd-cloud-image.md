+++
title = "Update on BSD Cloud Image"
date = 2021-05-17T01:05:27+00:00
[taxonomies]
tags = ["bsd", "cloud"]
+++
I've pushed some new images on [https://bsd-cloud-image.org/](https://bsd-cloud-image.org/):

* OpenBSD 6.9, [bsd.rd is now a compressed file](https://github.com/goneri/pcib/commit/7368ea62c2b117df7ee950d6297ee190b372e9a4)
* FreeBSD 13.0: [boot1.efifat does not exist anymore](https://github.com/virt-lightning/freebsd-cloud-images/commit/7e811070124295b787cc79b7c7a8283a383ff56f)
* DragonFly BSD 6.0.0, I've refreshed my [Cloud-Init PR](https://github.com/canonical/cloud-init/pull/904). Hopefully this time I will manage to get it merged.

These images also include a recent fix [for non-standard MTU values](https://github.com/canonical/cloud-init/commit/6fe1983777663a1a1136fd73dc50244f2d030be8).

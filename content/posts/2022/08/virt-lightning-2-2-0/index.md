+++
title = "Virt-Lightning 2.2.0"
date = 2022-08-23T22:59:36+00:00
[taxonomies]
tags = ["virt-lightning", "linux", "cloud"]
+++
[![](logo_no_text.png)](logo_no_text.png)

Release 2.2.0 of [Virt-Lightning](https://pypi.org/project/virt-lightning/2.2.0/), a lightweight CLI for libvirt which can serve as an alternative to Vagrant. It's also a stable API that you can use in Python to quickly spawn new VM, like you would do with a Cloud provider.  

Most of the new features come from contributors and I'm pretty happy with this.

**Changelog**

* Cosmetic documentation changes
* Don't try to fetch an image that already exists
* Add ability to boot old system with no virtio support
* Use Libvirt default settings when possible
* Use the VNC display by default
* Add support for OpenVSwitch (a.k.a OVS )bridge
* vl stop: avoid a Python backtrace if the VM doesn't exist

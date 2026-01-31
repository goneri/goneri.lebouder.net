+++
title = "eGPU, Wayland, Gnome3 and Fedora"
date = 2021-02-12T21:10:19+00:00
[taxonomies]
tags = ["tips", "linux", "gnome"]
+++
I've just got a Razer Core X that I use with a Radeon graphics card. By default Wayland, well Mutter actually, continues to use the Intel card of my T580.

To force it to use the second card, I had to add a udev rule and reboot. And that's all!

```
$ cat /etc/udev/rules.d/61-mutter-primary-gpu.rules
ENV{DEVNAME}=="/dev/dri/card1", TAG+="mutter-device-preferred-primary"
```

note: You need Gnome 3.38.2 for this to work properly. See: [https://gitlab.gnome.org/GNOME/mutter/-/merge\_requests/1562](https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1562)

update: the post was initially written for Fedora 33, but the fix also works great with Fedora 34.

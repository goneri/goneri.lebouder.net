+++
title = "0ad, Firewall and Fedora33"
date = 2021-02-21T02:19:17+00:00
description = "How to configure firewalld to allow connections to your 0AD game server by opening UDP port 20595."
[taxonomies]
tags = ["tips", "linux", "networking"]
+++
[![](0ad.jpg)](0ad.jpg)

By default, the firewall will prevent connection to your [0ad](https://play0ad.com/) server. To adjust that, you need to open up the port 20595 (UDP). This three lines create a Firewalld service called 0ad, attach it to the default zone and reload the firewall:

```
$ sudo firewall-cmd --permanent --new-service=0ad --set-description="0ad, A free, open-source game of ancient warfare" --add-port=20595/udp
$ sudo firewall-cmd --zone=FedoraWorkstation --add-service=0ad --permanent
$ sudo firewall-cmd --reload
```

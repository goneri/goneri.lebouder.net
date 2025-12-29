+++
title = "Sharing Internet connection on Fedora 40"
date = 2024-05-16T00:30:02+00:00
+++
It's surprisingly easy to build a router from a Fedora 40 box. Here eno1 is connected to my cable modem and enp8s0 is connected to my local network.

To NAT the Internet connection:

```shell
nmcli c add type ethernet con-name internet ifname eno1 connection.zone external ipv4.method auto
```

And set up the DHCP on the local network, the machine will use the IP 10.42.0.1 IP by default:

```shell
nmcli c add type ethernet con-name lebouder.net ifname enp8s0 connection.zone nm-shared ipv4.method=shared
```

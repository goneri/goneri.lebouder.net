+++
title = "Debian Vserver cheat sheet"
date = 2010-03-09T17:55:05+00:00
+++
This is just to keep track for myself on how to create a Vserver with Internet connectivity.

**Create the network interface** Edit `/etc/network/interfaces` and add:

```
auto dummy0
iface dummy0 inet static address 192.168.50.1 netmask 255.255.255.0
```

**Restart the network** `/etc/init.d/networking restart`

**Turn the NAT on**

```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

Replace eth0 with the network interface you use for your network access.

**Create the VM** `sudo vserver build build -n cyrus2.3 -m debootstrap --netdev dummy0 --interface 192.168.50.2/24 -- -d lenny`

**Enter the VM**

```
sudo vserver cyrus2.3 start
sudo vserver cyrus2.3 enter
```

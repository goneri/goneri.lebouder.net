+++
title = "UML avec rootstrap"
date = 2005-06-18T00:16:00+00:00
+++

## Introduction

Depuis, quelques temps, je voulais pouvoir m'installer une [Ubuntu](http://www.ubuntulinux.org/) et une [Debian](http://fr.wikipedia.org/wiki/Debian) Sarge afin de pouvoir mieux vérifier les paquages de [Klibido](http://klibido.sourceforge.net/).

[Sukria](http://www.sukria.net/fr/) m'avait expliqué qu'il utilisait [vserver](http://linux-vserver.org/) pour avoir un système virtuel tous en gardant de très bonne performance. Je pensais aussi a Xen Linux qui permet plus ou moins la même chose. Ce qui m'a découragé, c'est que dans les deux cas, il faut recompiler la kernellette et j'ai un chipset IT8212 qui n'est supporté que dans les branche -ac et -mm du Kernel, or, j'ai clairement la flemme de me prendre la tête a repasser sur un kernel "officiel" pour ensuite le patcher.

## Déploiment

Donc me voila parti sur [UserModeLinux](http://usermodelinux.org/) (UML) qui est certe plus lent, mais qui marche très bien sur un kernel classique. Pour l'installation de la partition, j'ai utilisé rootstrap.

```
apt-get install rootstrap user-mode-linux
```

La configuration est dans /etc/rootstrap/rootstrap.conf

```
[global]
fstype=ext2
initialsize=2048
freespace=0
modules=network mkfs mount debian uml umount
PATH=/bin:/sbin:/usr/bin:/usr/sbin

[network]
hostname=sarge
interface=eth0
transport=tuntap
host=192.168.0.69
uml=192.168.0.15
nameserver=213.228.0.95
gateway=192.168.0.1
```
+++
title = "S270 Wifi au boot sur Debian Sid"
date = 2006-01-07T03:11:00+00:00
+++

Ce soir, j'ai découvert que pour que les parametres wireless_* du /etc/network/interfaces l'interface doit déjà être "up".

Voila ce que ça donne :

```
iface eth1 inet dhcp
# j'up l'interface avant tout
pre-up ifconfig eth1 up
wireless_mode managed
wireless_channel 6
wireless_nick clara
wireless_key off
# sinon j'ai des problemes de stablitié du signal
wireles_rate 11M
# essid en dernier !
wireless_essid BZH
```

J'ai ce problème avec le chipset rt2500, ça mérite surement un rapport de bug :). A étudier…
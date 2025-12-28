+++
title = "Duide Antidote8 sur Debian Sid"
date = 2013-08-09T13:44:07+00:00
+++
J’ai acheté le correcteur orthographique [Antidote 8](http://www.druide.com/antidote.html) que j’ai installé hier. L’outil est vraiment impressionnant et agréable à utiliser.

L’installation sur Debian Sid n’est pas supportée, cependant son utilisation est possible. Je dois encore voir si je peux l’intégrer avec Firefox (Iceweasel) et Thunderbird (Icedove).

Installation
==========

`# apt-get install libx11-6 libxslt1.1 libvorbis0a libxrender1 libgstreamer-plugins-base0.10-0 libpulse0 libpulse0 libpulse-mainloop-glib0 libfreetype6libpulse-mainloop-glib0 libfontconfig1 libxext6 libicu48``# wget http://ftp.fr.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb
# dpkg -i libssl0.9.8_0.9.8o-4squeeze14_amd64.deb`

> `# wget http://ftp.fr.debian.org/debian/pool/main/i/icu/libicu44_4.4.1-8_amd64.deb
>
>
>
> `
>
> `# dpkg -i libicu44_4.4.1-8_amd64.deb`
>
>
>
> Pour éviter un problème avec les kernel \>= 3 il faut faire une petite manip présentée ici : http://www.debian-fr.org/certains-logiciels-dysfonctionnent-en-changeant-de-noyau-t42688.html`# wget https://mail.gnome.org/archives/evolution-list/2003-December/txtBEWSVk2eft.txt -O /tmp/uname.c
> $ (echo #define _GNU_SOURCE; cat /tmp/uname.c) > /tmp/uname.c
> $ gcc -shared -fPIC -ldl uname.c -o /opt/Druide/Antidote8/Programmes64/fake-uname.so`
>
>
>
> Il ne reste plus qu'a ajouter les deux lignes suivantes au début du script /opt/Druide/Antidote8/Programmes64/Antidote8.`export LD_PRELOAD=/opt/Druide/Antidote8/Programmes64/fake-uname.so
> export RELEASE=$(uname -r | sed 's/^\(...\)/\1.0-antidote-fix/g')`
>
>

+++
title = "thunderbird-2.0.0.23 built by Mozilla and Debian Squeeze"
date = 2009-09-03T16:40:04+00:00
+++
Mozilla still builds against libstdc++5...

```shell
/opt/thunderbird-2.0.0.23$ ./thunderbird
./thunderbird-bin: error while loading shared libraries: libstdc++.so.5: cannot open shared object file: No such file or directory
```

The solution is very simple. Just use libstdc++5 from Lenny:

```shell
wget http://ftp.fi.debian.org/debian/pool/main/g/gcc-3.3/libstdc++5_3.3.6-18_i386.deb
sudo dpkg -i libstdc++5_3.3.6-18_i386.deb
```

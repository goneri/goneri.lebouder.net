+++
title = "ext4 with barrier=1 and performance"
date = 2013-02-04T09:41:35+00:00
+++
The use of nobarrier provides a great performance gain on my laptop. I think I will continue with this approach even if my hard drive has no battery unit.

With ext4 (rw,noatime,errors=remount-ro,data=ordered)
----------

```
#fs_mark -t 4 -s 10240 -n 1000 -d /home/goneri/tmp/test # Version 3.3, 4 thread(s) starting at Mon Feb 4 10:35:47 2013
# Sync method: INBAND FSYNC: fsync() per file in write loop.
# Directories: no subdirectories used
# File names: 40 bytes long, (16 initial bytes of time stamp with 24 random bytes at end of name)
# Files info: size 10240 bytes, written with an IO size of 16384 bytes per write
# App overhead is time in microseconds spent in the test not doing file writing related system calls. FSUse% Count Size Files/sec App Overhead
o 84 4000 10240 35.2 113031
```

ext4 (rw,noatime,nobarrier,errors=remount-ro,commit=15,data=ordered)
----------

```
tosh-r630:/tmp$ fs_mark -t 4 -s 10240 -n 1000 -d ~/tmp/test # fs_mark -t 4 -s 10240 -n 1000 -d /home/goneri/tmp/test # Version 3.3, 4 thread(s) starting at Mon Feb 4 10:40:06 2013
# Sync method: INBAND FSYNC: fsync() per file in write loop.
# Directories: no subdirectories used
# File names: 40 bytes long, (16 initial bytes of time stamp with 24 random bytes at end of name)
# Files info: size 10240 bytes, written with an IO size of 16384 bytes per write
# App overhead is time in microseconds spent in the test not doing file writing related system calls. FSUse% Count Size Files/sec App Overhead 84 4000 10240 839.9 99672
```

+++
title = "Extract data from an Android phone"
date = 2021-07-11T10:29:24+00:00
+++
So, I've got an old phone with 35GB of pictures that I want to save. So far, I tried NextCloud sync, scp copy, GIO/MTP file. For all of those, it's a 12+ hour operation. And the real solution is to enable the developer mode on the phone and go straight to `adb`:

```
$ adb pull /sdcard/DCIM
/sdcard/DCIM/: 5825 files pulled. 31.9 MB/s (37517869453 bytes in 1122.166s)
```

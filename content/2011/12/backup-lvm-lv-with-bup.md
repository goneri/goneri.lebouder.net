+++
title = "backup LVM LV with bup"
date = 2011-12-31T00:11:50+00:00
+++
Bup is a backup software that use git for the storage. Bup import chunks of file to deduplicate large files.

> tosh-r630:\~/backup$cat /dev/mapper/virtualmachines-sarge | bup split -n virtualmachines-sarges
> bloom: adding 1 file (10967 objects).
> tosh-r630:\~/backup$bup join virtualmachines-sarges \> /tmp/sarges.img
> tosh-r630:\~/backup$file /tmp/sarges.img /tmp/sarges.img: x86 boot sector; GRand Unified Bootloader, stage1 version 0x3, stage2 address 0x2000, stage2 segment 0x200, GRUB version 0.94; partition 1: ID=0x83, active, starthead 1, startsector 63, 9976302 sectors; partition 2: ID=0x5, starthead 0, startsector 9976365, 498015 sectors, code offset 0x48

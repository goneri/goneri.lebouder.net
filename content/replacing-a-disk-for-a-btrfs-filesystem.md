+++
title = "Btrfs disk upgrade done wrong"
date = 2025-12-10T20:31:57+00:00
+++
I'm in the process to upgrade an existing Btrfs multi-disk filesystem (`/var/mnt/datapool`) and I made a mistake...

I went with a naive:

```
btrfs device add /dev/sde /var/mnt/datapool/
```

followed by:

```
btrfs device remove /dev/sda /var/mnt/datapool/
```

which was not totally wrong, and add the new disk and I remove the old one. Btrfs is now rebalancing the blocks from `/dev/sda` to`/dev/sde`. But it's also bloody slow, only 400MB have been moved after 6h.

I can track the progress with:

```
btrfs filesystem usage /var/mnt/datapool
```

And Btrfs prints some event in the Kernel logs that I can track with:

```
journalctl -exfk
```

Note for the Gonéri from the future, use `btrfs replace` next time! It will do (pretty much) a directly block by block copy of the old disk to the new one and it's **much faster**.

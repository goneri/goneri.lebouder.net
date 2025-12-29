+++
title = "NextCloud photos backups"
date = 2023-08-12T17:16:55+00:00
+++
I've been doing the backups for my family for years now. In the past, I used several different systems including rsync and [burp](https://burp.grke.org/).

Recently, I decided to stop hosting my own backup server and move to Nextcloud. I use the Nextcloud[ offer from Hetzner](https://www.hetzner.com/storage/storage-share) and I'm pretty happy with the result. I appreciate having a solution that just works without having to think about it.

Regarding the clients applications. The Nextcloud application on Android works fine but is also not really pleasant to use. I ended up buying the [FolderSync Pro](https://play.google.com/store/apps/details?id=dk.tacit.android.foldersync.full&hl=en&gl=US) application for myself. I strongly recommend it even if I would prefer a better free software solution. I use Webdav on Linux to synchronize my files. Both Nautilus and the davfs driver work as expected. MacOS is also able to mount the Webdav shares, this is a much better solution than the NextCloud application for Mac. However, iPhotos stores the pictures in some kind of local binary DB and there is no easy way to export them. iPhotos comes with an ["Export" feature](https://support.apple.com/en-ca/guide/photos/pht6e157c5f/mac) that is all manual and pathologically slow. But there is a solution! I recently discovered [osxphotos](https://github.com/RhetTbull/osxphotos) and it's an absolute gem.

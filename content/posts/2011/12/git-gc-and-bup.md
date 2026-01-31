+++
title = "git gc and bup"
date = 2011-12-31T00:34:23+00:00
[taxonomies]
tags = ["tips", "git", "backup"]
+++
To avoid the OOM killer after a `git gc` call on a bup repository:

```shell
$ git config --global pack.windowMemory 512m
$ git config --global pack.threads 10
```

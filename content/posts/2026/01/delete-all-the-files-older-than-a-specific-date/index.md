+++
title = "Delete all the files older than a specific date"
date = 2026-01-31T17:01:22+00:00
[taxonomies]
tags = ["tips", "ansible"]
+++

This is the first time I read about `-newermt` and it's pretty cool, the following command
will remove all the files older than Jan 1st, 2026:

```shell
find . ! -newermt "jan 01, 2026" -type f -delete
```

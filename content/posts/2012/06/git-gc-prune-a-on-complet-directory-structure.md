+++
title = "git gc --prune on a complete directory structure"
date = 2012-06-13T10:43:56+00:00
[taxonomies]
tags = ["tips", "git"]
+++
To run "git gc --prune" on a structure of subdirectories of git repositories, like for example a /git directory on a server:

```shell
find /git -type d -execdir sh -c '[ -f "description" ] && sudo git gc --prune' \;`
```

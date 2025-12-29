+++
title = "git gc --prune a on complet directory structure"
date = 2012-06-13T10:43:56+00:00
+++
To run "git gc --prune" on a structure of subdirectory of git repositories, like for example a /git directory on a server:

```shell
find /git -type d -execdir sh -c '[ -f "description" ] && sudo git gc --prune' \;`
```

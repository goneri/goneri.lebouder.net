+++
title = "Refresh all my git clones"
date = 2013-09-15T21:58:22+00:00
[taxonomies]
tags = ["tips", "git"]
+++
These are the commands I use to refresh all my git clones. For example, when I know I will be offline in the coming hours:

```
locate --regex '\.git$'|parallel 'cd {} && cd .. && echo $PWD && git fetch --all'
```

The use of GNU parallel is helpful to reduce the sync duration.

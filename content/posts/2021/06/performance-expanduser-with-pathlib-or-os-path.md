+++
title = "Performance: expanduser with pathlib or os.path"
date = 2021-06-23T18:28:19+00:00
[taxonomies]
tags = ["python", "performance"]
+++
Python 3 provides a new fancy library to manage pretty much all the path-related operations. This is a really welcome improvement since before that we had to use a long list of unrelated modules.

I recently had to choose between Pathlib and os.path to expand a string in the ~/path format to the absolute path. Since performance was important, I took the time to benchmark the two options:

```
#!/usr/bin/env python3

import timeit

setup = '''
from pathlib import PosixPath
'''
with_pathlib = timeit.timeit("abs_remote_tmp = str(PosixPath('~/.ansible/tmp').expanduser())", setup=setup)

setup = '''
from os.path import expanduser
'''

with_os_path = timeit.timeit("abs_remote_tmp = expanduser('~/.ansible/tmp')", setup=setup)

print(f"with pathlib: {with_pathlib}\nwith os.path: {with_os_path}")
```

os.path is about 4 times faster for this very specific case. The fact that we need to instantiate a PosixPath object has an impact. Also, once again we observe a nice performance boost with Python 3.8 onwards.

[<img alt="" src="performance2.png" height="340" width="605" />](performance2.png)

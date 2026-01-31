+++
title = "Create thumbnail images of a set of pictures"
date = 2015-01-03T14:10:32+00:00
[taxonomies]
tags = ["tips", "python"]
+++
Load 4 pictures at a time from the input directory and create thumbnail montage images:

```
#!/usr/bin/env python3

import glob
import subprocess

inputs = glob.glob('input/*.JPG')

cpt = 0
while len(inputs) > 0:
to_process = inputs[:4] + ['logo:', 'logo:', 'logo:']
inputs = inputs[4:]
cpt += 1
subprocess.call(["montage"] + to_process[:4] + ["-geometry", "800x600+2+2", "final/final_%02d.jpg" % cpt])
```

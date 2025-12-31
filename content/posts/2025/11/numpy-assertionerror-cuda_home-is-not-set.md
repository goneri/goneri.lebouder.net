+++
title = "numpy: AssertionError: CUDA_HOME is not set"
date = 2025-11-07T23:11:40+00:00
+++
To get Numpy to build on RHEL9, you need to install nvcc and export CUDA\_HOME, e.g:

```
$ sudo dnf install -y rpm -ql cuda-nvcc-13-0
$ sudo ln -s /usr/local/cuda-13.0 /usr/local/cuda
$ pip install numpy
```

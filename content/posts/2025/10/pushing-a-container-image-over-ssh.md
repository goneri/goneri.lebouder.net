+++
title = "Pushing a container image over SSH"
date = 2025-10-20T18:00:04+00:00
+++
I recently faced the situation where my registry was down and after a bit of digging, I ended up with this solution. In this example my image is called `quay.io/goneri/my-image:latest`:

```
podman image scp quay.io/goneri/my-image:latest ec2-user@your-host::quay.io/goneri/my-image:latest
```

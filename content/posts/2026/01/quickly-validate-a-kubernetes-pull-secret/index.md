+++
title = "Quickly-validate-a-kubernetes-pull-secret"
date = 2026-01-28T14:13:52+00:00
+++

This two commands are handy to quickly valide that a PullSecret secret is correct:

```shell
kubectl get secret my-secret -o jsonpath='{.data.\.dockerconfigjson}' | base64 --decode > ~/tmp/auth.json
podman pull --authfile ~/tmp/auth.json quay.io/some/image
```

+++
title = "List all pods by age that are not from OpenShift"
date = 2025-09-10T15:08:51+00:00
+++
Get a flat list of all the pods, except those coming from openshift namespaces

```
$ oc -o json get pods -A --sort-by=.status.startTime |jq '.items[].metadata|select(.namespace | startswith("openshift") | not)|pick(.name, .namespace, .creationTimestamp)'
```

and to find the largest pods by memory

```
$oc adm top pods -A --sort-by=memory
```

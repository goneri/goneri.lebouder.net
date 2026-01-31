+++
title = "Connect to ZooKeeper over TLS/SSL"
date = 2021-10-15T17:39:23+00:00
[taxonomies]
tags = ["tips", "security"]
+++
[<img alt="" src="zk_logo.png" height="209" width="147" />](zk_logo.png)

It's surprisingly tricky to connect to a ZooKeeper cluster over TLS/SSL using the zkCli.sh command. You've got to wrap the command and pass some extra incantations. Here is the script I use. My certificates are in /etc/zookeeper/ca, so you may need to adjust that to match your local installation.

```
#!/bin/bash

ZK_CLIENT_HEAP="${ZK_CLIENT_HEAP:-256}"
export ZK_CLIENT_SSL="-Dzookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty -Dzookeeper.ssl.keyStore.location=/etc/zookeeper/ca/keystores/server.pem -Dzookeeper.ssl.trustStore.location=/etc/zookeeper/ca/certs/cacert.pem -Dzookeeper.client.secure=true"
export CLIENT_JVMFLAGS="-Xmx${ZK_CLIENT_HEAP}m $ZK_CLIENT_SSL $CLIENT_JVMFLAGS"
/opt/zookeeper/bin/zkCli.sh -server my-host-fqdn:2281
```

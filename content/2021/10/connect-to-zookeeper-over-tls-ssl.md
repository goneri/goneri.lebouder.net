+++
title = "Connect to Zookeeper over TLS/SSL"
date = 2021-10-15T17:39:23+00:00
+++
[<img alt="" src="/wp-content/uploads/2021/10/zk_logo.png" height="209" width="147" />](/wp-content/uploads/2021/10/zk_logo.png)

It's surprisingly tricky to connect to a Zookeeper cluster over TLS/SSL using the zkCli.sh command. You've got to wrap the command and pass some extra incantations. This is the script I use. Here my certificates are in /etc/zookeeper/ca, you may need to adjust that to match your local installation.

```
#!/bin/bash

ZK_CLIENT_HEAP="${ZK_CLIENT_HEAP:-256}"
export ZK_CLIENT_SSL="-Dzookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty -Dzookeeper.ssl.keyStore.location=/etc/zookeeper/ca/keystores/server.pem -Dzookeeper.ssl.trustStore.location=/etc/zookeeper/ca/certs/cacert.pem -Dzookeeper.client.secure=true"
export CLIENT_JVMFLAGS="-Xmx${ZK_CLIENT_HEAP}m $ZK_CLIENT_SSL $CLIENT_JVMFLAGS"
/opt/zookeeper/bin/zkCli.sh -server my-host-fqdn:2281
```

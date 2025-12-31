+++
title = "Getting BURP to use Puppet CA"
date = 2013-10-16T13:20:56+00:00
+++
I'm a big fan of [BURP](http://burp.grke.org/) to maintain my backups. This article explains how to reuse the PuppetMaster CA for authentication. I use Debian burp package on Wheezy.

First, you need to generate the dhfile.pem on both the server and the agent:

```
openssl dhparam -outform PEM -out /etc/burp/dhfile.pem 1024
```

The server
----------

The configuration is in /etc/burp/burp-server.conf:

```
mode = server
(...)
# ca_conf = /etc/burp/CA.cnf
# ca_name = burpCA
# ca_server_name = burpserver
# ca_burp_ca = /usr/sbin/burp_ca
(...)
ssl_cert_ca = /var/lib/puppet/ssl/certs/ca.pem
ssl_cert = /var/lib/puppet/ssl/ca/signed/newpuppet.lebouder.net.pem
ssl_key = /var/lib/puppet/ssl/private_keys/newpuppet.lebouder.net.pem
ssl_key_password = password
ssl_dhfile = /etc/burp/dhfile.pem
(...)
```

The agent
----------

The configuration file is /etc/burp/burp.conf:

```
mode = client
port = 4971
server = newpuppet.lebouder.net
ssl_cert_ca = /var/lib/puppet/ssl/certs/ca.pem
ssl_cert = /var/lib/puppet/ssl/certs/newclient.lebouder.net.pem
ssl_key = /var/lib/puppet/ssl/private_keys/newclient.lebouder.net.pem
ssl_peer_cn = newpuppet.lebouder.net
(...)
```

newpuppet.lebouder.net is the Puppet server.

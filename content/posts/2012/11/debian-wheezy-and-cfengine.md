+++
title = "Debian Wheezy and cfengine"
date = 2012-11-17T20:10:24+00:00
[taxonomies]
tags = ["tips", "debian", "linux"]
+++
How to bootstrap a cfengine node with Debian Wheezy Cfengine:

```shell
# cp /usr/share/doc/cfengine3/example_config/* /etc/cfengine3/
# sed -i 's,"/var/lib/cfengine3/inputs","/etc/cfengine3",' /etc/cfengine3/update.cf
# sed -i 's,RUN_CFEXECD=0,RUN_CFEXECD=1,' /etc/default/cfengine3
# /etc/init.d/cfengine3 restart
# cf-agent --bootstrap --policy-server 2a01:e35:242d:e930:250:XXXX:XXXX:XXXXX
```

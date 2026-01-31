+++
title = "firewalld: add a new service"
date = 2024-05-16T18:40:35+00:00
[taxonomies]
tags = ["tips", "linux", "networking"]
+++
Create a new service entry:

```shell
firewall-cmd --permanent --new-service=ollama
```

Associate the right port with new service:

```shell
firewall-cmd --permanent --service=ollama --add-port=11434/tcp
```

Restart the firewalld, so it's aware of the new service:

```shell
firewall-cmd --reload
```

Finally, associate the service with the Zone. I don't use `--permanent` here on purpose. This way the association will be lost when I will reboot the machine:

```shell
firewall-cmd --add-service=ollama --zone=nm-shared
```

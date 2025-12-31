+++
title = "How to start minishift on Fedora-33"
date = 2020-11-05T19:43:51+00:00
+++
**update: minishift is basically dead and won't support OpenShift 4. You probably want to use [crc](https://developers.redhat.com/blog/2019/09/05/red-hat-openshift-4-on-your-laptop-introducing-red-hat-codeready-containers/) instead.**

I just spent too much time trying to start [minishift](https://github.com/minishift/minishift) with my user account. After 3 hours fighting with permission issues between libvirt and the `~/.minishift` directory, I've finally decided to stay sane and use `sudo`... This is how I start minishift on my Fedora 33.

### Install and start libvirt ###

```
sudo dnf install -y libvirt qemu-kvm
sudo systemctl start libvirtd
```

### Fetch and install minishift and the kvm driver ###

```
sudo dnf install -y origin-clients
curl -L https://github.com/minishift/minishift/releases/download/v1.34.3/minishift-1.34.3-linux-amd64.tgz|sudo tar -C /usr/local/bin -xvz minishift-1.34.3-linux-amd64/minishift  --strip-components=1
sudo curl -L https://github.com/dhiltgen/docker-machine-kvm/releases/download/v0.10.0/docker-machine-driver-kvm-centos7 -o /usr/local/bin/docker-machine-driver-kvm
sudo chmod +x /usr/local/bin/docker-machine-driver-kvm
```

### Start minishift (with sudo...) ###

sudo minishift

### And configure the local user ###

```
sudo cp -r /root/.kube /home/goneri
sudo chown -R goneri:goneri /home/goneri/.kube
```

+++
title = "Installing CRC on CoreOS"
date = 2025-12-18T20:06:41+00:00
+++
My local home server runs on CoreOS and today I went through the installation of Red Hat Code Ready Container, aka CRC

Download

Go on [https://console.redhat.com/openshift/create/local](https://console.redhat.com/openshift/create/local) and download both:

* the crc binary, which they call OpenShift Local
* and the Pull secret

Preparation

The first thing to do is to allow the installation of local packages

and install libvirt:

```
sudo bootc usr-overlay
sudo dnf install -y libvirtd
```

Add yourself in the libvirt group:

```
sudo usermod -a -G libvirt core
```

Restart the polkit.service and libvirtd to run the new policies:

```
sudo systemctl restart polkit.service
sudo systemctl restart libvirtd
```

Set-up the local CRC installation, first extract the crc archive and copy the crc binary in `/usr/local/bin`. You can now start the installation:

```
crc config set preset openshift
# optional, turn it "true", to be able to access the host from the VM
crc config set host-network-access true
crc setup

```

And finally, deploy the cluster:

```
crc start --cpus=12 --memory=40000 -d 100
```

At the end of the installation, crc add an extra line to your `/etc/hosts`, you probably want to copy it to your local desktop machine in order to access the cluster through your web browser, and set-up a port redirection like this. I use sudo to be able to bind on my local port `443`:

```
sudo ssh -L 443:127.0.0.1:443 -L 6443:127.0.0.1:6443 -i ~/.ssh/id_ed25519 core@your-coreos-box
```

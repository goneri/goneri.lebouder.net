+++
title = "Run Virt-Lightning on CoreOS"
date = 2026-01-09
[taxonomies]
tags = ["tips", "linux", "virt-lightning"]
+++

[Virt-Lightning](https://virt-lightning.org/) is my pet-project to quickly start Cloud VMs
on a Libvirt Hypervisor and these are some notes I took to run it on [Fedora CoreOS](https://fedoraproject.org/coreos/).

First, you need to install `libvirt` and `uv`:

```shell
sudo bootc usr-overlay
sudo dnf install -y uv libvirt-devel gcc python3-devel qemu-kvm qemu-img libvirt mkisofs
sudo systemctl restart polkit.service
sudo systemctl enable --now libvirtd
sudo usermod --append --groups libvirt core
```

By default, CoreOS is an immutable Operating System. `bootc usr-overlay` enables write operations,
but they will be lost after the next reboot.

Then, create the image directory:

```shell
sudo mkdir -p /var/lib/virt-lightning/pool/upstream
sudo chown -R qemu:qemu /var/lib/virt-lightning/pool
sudo chown -R core /var/lib/virt-lightning/pool/upstream
sudo chmod 775 /var/lib/virt-lightning
sudo chmod 775 /var/lib/virt-lightning/pool /var/lib/virt-lightning/pool/upstream
```

And you're good to go, you can deploy a VM with just one command:

```shell
uvx virt-lightning start fedora-43 --memory 2048
```

Or if you're adventurous, you can try the [Git version](https://github.com/virt-lightning/virt-lightning):

```shell
uvx --from git+https://github.com/virt-lightning/virt-lightning vl start fedora-43 --memory 2048
```

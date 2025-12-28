+++
title = "CI of the Ansible modules for VMware: a retrospective"
date = 2020-08-21T20:13:14+00:00
+++
[![Simple VMware Provisioning, Management and Deprovisioning](https://www.ansible.com/hs-fs/hubfs/2016_Images/Overview/ansible-vmware-blog-300.png?width=300&height=200&name=ansible-vmware-blog-300.png)](https://www.ansible.com/integrations/infrastructure/vmware?hsLang=en-us)

Since January 2020, every new Ansible VMware pull request is tested by the CI against a real VMware lab. Creating the CI environment against a real VMWare lab has been a long journey, which I'll share in this blog post.

Ansible VMware provides more than 170 modules, each of them dedicated to a specific area. You can use them to manage your ESXi hosts, the vCenters, the vSAN, do the common day-to-day guest management, etc.

Our modules are maintained by a community of contributors, and a large number of the Pull Requests (PR) are contributions from newcomers. The classic scenario is a user who's found a problem or a limitation with a module, and would like to address it.

This is the reason why our contributors are not necessary developers. The average contributor doesn't necessarily have advanced Python experience. We can hardly ask them to write Python unit-tests. Requiring this level of work creates a barrier to contribution. this would be a source of confusion and frustration and we would lose a lot of valuable contributions. However, they are power users. They have a great understanding of VMware and Ansible, and so we maintain a test playbook for most of the modules.

Previously, when a new change was submitted, was running the light Ansible sanity test-suite and an integration test against govcsim, a VMware API simulator ([https://github.com/vmware/govmomi/tree/master/vcsim](https://github.com/vmware/govmomi/tree/master/vcsim)).

govcsim is a handy piece of software; you can start it locally to mock a vSphere infrastructure. But it doesn't fully support some important VMware components like the network devices or datastore. As a consequence, the core-reviewers were asked to download the changeset locally, and run the functional tests against their own vSphere lab.

In our context, a vSphere lab is:

\- a vCenter instance

\- 2 ESXi

\- 2 NFS datastores, with some pre-existing files.

We also had the challenge in our test environment. Functional tests destroy or create network switches, enable IPv6, add new datastores, and rarely if ever restored the system to initial configuration once complete. Leaving the labs in disarray, and compounding with each series of tests. Consequently, the reviews were slow, and we were wasting days fixing our infrastructures. Since the tests were not reproducible and done locally, it was hard to distinguish set-up errors from actual issues and therefore it was hard to provide meaningful feedback to contributors: Is this error coming from my set-up? I need to manually copy/past the error with the contributor, sometime several days after the initial commit.

This was a frustrating situation for us, and for the contributors. But well, we've spent years doing that...

You may find we like to suffer, which is probably true to some extent, but the real problem is that it's rather complex to automate the full deployment of a lab. vSphere is an appliance VM in the OVA format. It has to be deployed on an ESXi. Officially, the ESXi can't be virtualized, unless they run on an ESXi themselves. In addition, we use Evaluation licenses, and as a consequence, we cannot rely on features like snapshotting, and we have to redeploy our lab every 60 days.

We can do better! Some others did!
----------

The Ansible network modules were facing similar challenges. Network devices are required to fully validate a change, but it's costly to stack and maintain operation of hundreds of devices just for validation.

They've decided to invest in OpenStack and a CI solution called Zuul-CI (https://zuul-ci.org/). I don't want to elaborate too much on Zuul since the topic itself is worth a book. But basically, everytime a change gets pushed, Zuul will spawn a multi node test environment, prepare the test execution using ... Ansible, Yeah! And finally, run the test and collect the result. This environment makes use of appliances coming from the vendors. It's basically just a VM. OpenStack is pretty flexible for this use-case, especially when you've got top-notch support with the providers.

Let's build some VMware Cloud images!
----------

To run a VM in a cloud environment, it has to match the following requirements:

* use one single disk image, a qcow2 in the case of OpenStack.
* supports the hardware exposed by the hypervisor, qemu-kvm in our case
* configures itself according to the metadata information exposed by the cloud provider (IP, SSH keys, etc). This service is handled by Cloud-init most of the time.

### ESXi cloud image ###

For ESXi, the first step was to deploy ESXi on libvirt/qemu-kvm. This works fine as we avoid virtio. And with a bit more effort, we can automate the process ( [https://github.com/virt-lightning/esxi-cloud-images](https://github.com/virt-lightning/esxi-cloud-images) ). But our VM is not yet self-configuring. We need an alternative to Cloud-init. This is what esxi-cloud-init ( [https://github.com/goneri/esxi-cloud-init/](https://github.com/goneri/esxi-cloud-init/) ) will do for us. It reads the cloud metadata and prepares the network configuration of the ESXi host, and it also injects the SSH keys.

The image build process is rather simple once you've got libvirt and virt-install on your machine:

`$ git clone https://github.com/virt-lightning/esxi-cloud-images`

$ cd esxi-cloud-images

$ ./build.sh \~/Downloads/VMware-VMvisor-Installer-7.0.0-15525992.x86\_64.iso

(...)

$ ls esxi-6.7.0-20190802001-STANDARD.qcow2

[<img src="https://asciinema.org/a/349250.png" width="836" />](https://asciinema.org/a/349250)

The image can run on OpenStack, but also on libvirt. Virt-Lightning (https://virt-lightning.org/) is the tool we use to spawn our environment locally.

![](https://lh6.googleusercontent.com/rg2ydv_dKbG_8G1rKHzv8FiY05Pb9zBJNh9EWKGEZafsEqE7kyKFDiEGkOw9bGc8aNRWT75j5OytgCTPF5gsnetIMD4dwaVRKgk_Bp18GljioLziB14Q1U32lwLcD-83T7NlOps)

### vCenter cloud image too? ###

*update: See [Ansible: How we prepare the vSphere instances of the VMware CI](https://goneri.lebouder.net/2020/12/14/ansible-how-we-prepare-the-vsphere-instance-for-the-vmware-ci/) for a more detailed explaination of the VCSA deployment process.*

We wanted to deploy vCenter on our instance, but this is daunting. vCenter has a slow installation process, it requires an ESXi host, and is extremely sensitive to any form of network configuration changes...

So the initial strategy was to spawn a ESXi instance, and deploy vCenter on it. This is handled by ansible-role-vcenter-instance ( [https://github.com/goneri/ansible-role-vcenter-instance](https://github.com/goneri/ansible-role-vcenter-instance) ). The full process takes about 25m.

We became operational but the deployment process overwhelmed our lab. Additionally, the ESXi instance (16GB of RAM) was too much for running on a laptop. I started investigating new options.

Technically speaking, the vCenter Server Appliance or VCSA, is based on Photon Linux, the Linux distribution of VMware, and the VM actually comes with 15 large disks. This is a bit problematic since our final cloud image must be a single disk and be as small as possible. I developed this strategy:

1. connect on the running VCSA, move all the content from the partition to the main partition, and drop the extra disk from the /etc/fstab
2. do some extra things regarding the network and Cloud-init configuration.
3. stop the server
4. extract the raw disk image from the ESXi datastore
5. convert it to the qcow2 format
6. and voilà! You've got a nice cloud image of your vCenter.

All the steps are automated by the following tool: [https://github.com/virt-lightning/vcsa\_to\_qcow2](https://github.com/virt-lightning/vcsa_to_qcow2). It also enables virtio for better performance.

### Preparing development environment locally ###

To simplify the deployment, I use the following tool: https://github.com/goneri/deploy-vmware-ci. It will use virt-lightning to spawn the nodes, and do the post-configuration with Ansible. It reuses the roles that we consume in the CI to configure the vCenter, the host names, and populate the datastore.

In this example, I use it to start my ESXi environment on my Lenovo T580 laptop; the full run takes 15 minutes: https://asciinema.org/a/349246

Being able to redeploy a work environment in 15 minutes has been a life changer. I often recreate it several times a day. In addition, the local deployment workflow reproduces what we do in the CI, it's handy to validate a changeset, or troubleshoot a problem.

### The CI integration ###

Each Ansible module is different, which makes for different test requirements. We've got 3 topologies:

* vcenter\_only: only one single vCenter instance)
* vcenter\_1esxi\_with\_nested: one vCenter with an ESXi, this ESXi is capable of starting a nested VM.
* vcenter\_1\_esxi\_without\_nested: the same. but this time, we don't start nested VM. Compared to the previous case, this set-up is compatible with all our providers.
* vcenter\_2\_esxi\_without\_nested: well, like the previous one, but with a second ESXi, for instance to test ha or migration.

The nodeset definition is done in the following file: [https://github.com/ansible/ansible-zuul-jobs/blob/master/zuul.d/nodesets.yaml](https://github.com/ansible/ansible-zuul-jobs/blob/master/zuul.d/nodesets.yaml)

We split the hours long test execution time on the different environments. An example of job result:

![](https://rvf.wax.mybluehost.me/wp-content/uploads/2020/08/image-8.png?w=716)

As you can see, we still run govcsim in the CI, even if it's superseded by a real test environment. Since govcsim jobs run faster, we assume that failure would also fail against the real lab and abort the other jobs. This is a way to save time and resources.

I would like to thank Chuck Copello for the helpful review of this blog post.

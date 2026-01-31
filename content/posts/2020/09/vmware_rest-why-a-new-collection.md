+++
title = "vmware_rest: why a new Ansible Collection?"
date = 2020-09-29T17:03:03+00:00
[taxonomies]
tags = ["ansible", "vmware"]
+++
**vmware.vmware\_rest** ([https://galaxy.ansible.com/vmware/vmware\_rest](https://galaxy.ansible.com/vmware/vmware_rest)) is a new Ansible Collection for VMware. You can use it to manage the guests of your vCenter. If you're familiar with Ansible and VMware, you will notice this collection overlaps with some features of community.vmware. You may think the two collections are competing and that it's a waste of resources. It's not that simple.

A bit of context will be necessary to fully understand why it’s not exactly the case. The development of the community.vmware collection started during the vCenter 6.0 cycle. At this time, the de facto SDK to build Python applications was pyvmomi, which you may know as the vSphere SDK for Python. This Python library relies on the SOAP interface that has been around for more than a decade. By comparison, the vSphere REST interface was still a novelty. The support of some important APIs were missing and documentation was limited.

Today, the situation has evolved. Pyvmomi is not actively maintained anymore and some new services are only exposed through the REST interface; a good example is the tagging API. VMware has also introduced a new Python SDK called vSphere Automation SDK ([https://github.com/vmware/vsphere-automation-sdk-python](https://github.com/vmware/vsphere-automation-sdk-python)) to consume this new API. For instance, this is what community.vmware\_tag\_info uses underneath.

This new SDK comes at a cost for users. They need to pull an extra Python dependency in addition to pyvmomi and to make matters worse, this library is not on PyPI (See: [https://github.com/vmware/vsphere-automation-sdk-python/issues/38](https://github.com/vmware/vsphere-automation-sdk-python/issues/38)), Python's official library repository. They need to install it from GitHub instead. This is a source of confusion for our users.

From a development perspective, we don't like when a module needs to load a gazillion Python dependencies because this slows down the execution time and it's a source of complexity. But we cannot ditch pyvmomi immediately because a lot of modules rely on it. We can potentially rewrite these modules to use the vSphere Automation SDK.

These modules are already stable and of high quality. Many users depend on them. Modifying these modules to use the vSphere Automation SDK is risky. Any single regression would have a wide impact.

Our users would be frustrated by such a transition, especially because it would bring absolutely zero new features to them. This also means we would have to reproduce the exact same behavior, and we would miss an opportunity to improve the modules.

Technically speaking, an application that consumes a REST interface doesn't really need an SDK. It can be handy sometimes, for instance for the authentication, but overall the standard HTTP client should be enough. After all, the 'S' of REST stands for Simple for a reason.

The vSphere REST API is not always consistent, but it's well documented. VMware maintains a tool called vmware-openapi-generator ([https://github.com/vmware/vmware-openapi-generator](https://github.com/vmware/vmware-openapi-generator)) to extract it in a machine compatible format (Swagger 2.0 or OpenAPI 3).

During our quest for a solution to this Python dependency problem, we've designed a Proof of Concept (PoC). It was based on a set of modules with no dependency on any third-party library. And of course, these modules were auto-generated. We've mentioned the conclusion of the PoC back in March during the VMware / Ansible weekly meeting ([https://github.com/ansible/community/issues/423](https://github.com/ansible/community/issues/423)).

The feedback convinced us we were on the right path. And here we go, 5 months later. The first beta release of **vmware.vmware\_rest** has just been announced on [Ansible's blog](https://www.ansible.com/blog/introducing-the-vmware-rest-ansible-content-collection)!

+++
title = "How to speed up your (API client) modules"
date = 2020-10-13T18:54:03+00:00
+++
https://www.slideshare.net/goneri/how-to-speed-up-your-api-client-modules

The slide deck of my presentation for AnsibleFest 2020. It focus on the modules designed to interact with a remote service (REST, SOAP, etc). In general these modules just wrap a SDK library, the presentation explains how to improve the performance. I actually use this strategy ( [ansible\_turbo.module](https://github.com/ansible-collections/cloud.common/blob/main/README_ansible_turbo.module.rst) ) with the [vmware.vmware\_rest collection](https://github.com/ansible-collections/vmware.vmware_rest) to speed up the modules.

[how-to-speed-up-your-api-client-modules (PDF)](how-to-speed-up-your-api-client-modules.pdf)[Download](how-to-speed-up-your-api-client-modules.pdf)

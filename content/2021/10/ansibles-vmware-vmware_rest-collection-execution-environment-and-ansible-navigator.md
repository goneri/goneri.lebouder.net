+++
title = "Ansible's vmware.vmware_rest collection, Execution Environment and ansible-navigator"
date = 2021-10-19T19:27:25+00:00
+++
Ansible-Navigator is a new terminal base UI for Ansible. It aims to provide an alternative to the different ansible commands that you probably already familiar with. To learn more about Ansible-Navigator, a couple of recent blog posts on [Ansible Blog](https://www.ansible.com/blog/topic/ansible-navigator) cover this new tool. The Execution Environment, or just EE, is also a rather recent concept. With a EE Ansible and all its dependencies are shipped as a single container. You don't need anymore to care about the Python version, the virtualenv, the collections and Python dependency.

Ansible-Navigator provides an interface that is inspired by ansible-playbook. In this example we will see how we can use the CLI to run a playbook. My pass some credentials through environment variables, we will also see how to expose them properly.

The first thing is to prepare a `ansible-navigator.yml` file in your project directory.

```yaml
---
ansible-navigator:
   execution-environment:
     container-engine: podman
     enabled: True
     image: myregister/ansible-automation-platform-21-ee-supported-rhel8:2.1.0
     pull-policy: never
     environment-variables:
        pass:
          - VMWARE_VALIDATE_CERTS
          - VMWARE_HOST
          - VMWARE_PASSWORD
          - VMWARE_USER
          - ESXI1_PASSWORD
          - ESXI1_HOSTNAME
          - ESXI1_USERNAME
```

The `image` key point on the container, I use a Fedora and Podman is the default for container. I ensure Navigator use the right engine with the `container-engine: podman` configuration. I use the `environment-variables` section to list all the variables that I want to expose in my container. If you want to read about all the other configuration options, just read the documentation at [https://ansible-navigator.readthedocs.io/en/latest/](https://ansible-navigator.readthedocs.io/en/latest/).

If your playbook depends on some roles, for instance within a `roles` directory, it's important to call `ansible-navigator` from the root directory of your project. Otherwise, the roles won't be reachable from within the container. If your roles are maintained at a different location, you can still expose their directories with the [volume-mounts](https://ansible-navigator.readthedocs.io/en/latest/settings/?highlight=volume-mounts#the-ansible-navigator-settings-file) option. This is in my opinion slightly less elegant.

```shell
[goneri@t580 targets]$ ls -lh
total 416K
-rw-r--r--. 1 goneri goneri  469 Oct 19 15:09 ansible-navigator.yml
drwxrwxr-x. 2 goneri goneri    6 Oct 19 15:39 playbooks
drwxrwxr-x. 2 goneri goneri    6 Oct 19 15:39 roles
```

Now, I can just run my playbook with: `ansible-navigator run --mode stdout playbooks/vcenter_vm_scenario1`

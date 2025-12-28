+++
title = "Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!"
date = 2021-09-22T15:19:47+00:00
+++
```
TASK [helm : Copy test chart] **************************************************
fatal: [localhost]: FAILED! => {"changed": false, "checksum": "8b41aa269bd850134cd95bd27343edf6d4ed2e30", "msg": "Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!"}
```

Ah, this is one of the most irritating message that you can get when you use Ansible in a venv and SELinux. The problem should not happen anymore since this [commit](https://github.com/ansible/ansible/commit/4c5ce5a1a9e79a845aff4978cfeb72a0d4ecf7d6) that was first released in Ansible core 2.11.5, thanks David Moreau Simard for the information!. If you cannot upgrade, you can continue to read. This article we will quickly explain the problem and cover our options.

`copy` or `selinux` are two Ansible modules that depends on some system binary libraries. These binary libraries are linked/build using the Python of the system, on RHEL8 it's Python3.6. So it you use the Python 3.6 of the system, everything should be all right. You may just need to install `python3-selinux` if it's not already installed.

Things are getting more difficult if you use a virtualenv, and it's often a good idea to use a virtualenv. Here you two options:

If the Python3 version of your virtualenv is close enough with the version of the one of the system, you can use the [selinux](https://pypi.org/project/selinux/) package from Pypi. When a module will try to interact with the `selinux` module, this module will pretend to be the right person and will actually redirect the request the Python module from the system. It works well most of the time and pretty much the single way to do SElinux operation from a venv.

If you Python version is too new comparing to the system, Pypi's selinux will raise an error like this one:

```
ImportError: cannot import name '_selinux'
```

And in this case, you've got this second option. Here we assume that you don't really care about SElinux. For instance you use Ansible's copy module just to duplicate a file once. In this case, the whole SElinux war machine is not necessary. You can use [selinux-please-lie-to-me/](https://pypi.org/project/selinux-please-lie-to-me/), it's another Pypi module and it's similar to Pypi's SElinux module. The main difference is that this time, it will just tell Ansible that SELinux is off on the system and it can bypass it.

Oh! There is yet another option, you can overload the `ansible_python_interpreter` just for problematical task.

```
    - copy:
        src: /etc/fstab
        dest: /tmp/fstab
      vars:
        ansible_python_interpreter: /usr/bin/python3
```

Which one should I use? The `ansible_python_interpreter` creates a dependency with the system that is often annoying. I prefer to avoid this strategy. Overall it's better to use Pypi's SELinux because it will preserve the interaction with SELinux, but sometime, the delta between the version of Python is too important and the system binary module just cannot be load. In this case, use `selinux-please-lie-to-me` as a fallback option. Just remember that this Python module will silently inhibit all the SElinux operations.

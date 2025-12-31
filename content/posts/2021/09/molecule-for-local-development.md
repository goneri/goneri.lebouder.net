+++
title = "Ansible Molecule, how to use the local copy of the dependencies"
date = 2021-09-22T13:28:52+00:00
+++
The community.okd collection depends on kubernetes.core. It uses [Molecule](https://molecule.readthedocs.io/en/latest/) to run the tests. We can call it using either the Makefile and the `make molecule` command. We can also install molecule manually with pip and run it with `molecule test`.

When I work on community.okd, I often need to also adjust the kubernetes.core collection. By default Molecule fetches the dependencies silently from internet. This is done during either the `prerun` or the `dependency` steps. The mechanism is handy when you focus on one single collection at a time. But in my case, it's a bit annoying. The clean copy of kubernetes.core overwrites my local changes and prevents the testing of my local copy of the dependency.

This is how I ensure Molecule uses my local copy of the collections. I store them in the default location \~/.ansible/collections/ansible\_collections.

In molecule/default/molecule.yml I set the following key to turn off the `prerun`:

```
prerun: false
```

and I set the following block in the `dependency:` section:

```
 dependency:
   name: galaxy
   enabled: False
```

This will turn off the dependency resolver. Molecule won't call galaxy anymore to fetch the `roles` and the `collections` defined in the galaxy.yml.

You're done; as a bonus, the startup of `molecule` should be slightly faster!

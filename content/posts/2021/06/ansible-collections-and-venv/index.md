+++
title = "Ansible collections and venv"
date = 2021-06-02T17:46:10+00:00
[taxonomies]
tags = ["ansible", "python"]
+++
I work on a large number of collections and in order to test them properly, I have to switch between the Python versions and the associated PyPI dependencies. Nothing special here, this is pretty much the life of all of us who work on the Ansible collections.

Initially, I was maintaining a set of clean Python virtual environments. Basically, one per version of Python. And I was juggling between them. Sadly, it's easy to lose track of what's going on. Every time I was switching to a different collection, I had to pull a new set of dependencies and the order was never the same.

I ended up frustrated by the wasted time spent looking at the `pip freeze` output to understand some oddity. It's so easy to mess up the whole cathedral. A good example is that I frequently use `pip install -e git/something` to install a local copy of a library. And as a result, any change there can potentially nuke the fragile little creature.

[![](800px-incendie_de_la_fleche_en_1822.jpg)](800px-incendie_de_la_fleche_en_1822.jpg)

So now, I use another approach. I've got a script that spawns a virtual environment on the fly, pulls the right dependencies and initializes the shell. It may sound like a trivial thing, but I actually use it several times every day and I don't call `pip freeze` that much.

For instance, if I need to work with Ansible 2.10 and Python 3.10, I just need to do:

```
$ cd .ansible/collections/ansible_collections/vmware/vmware_rest
$ source ~/bin/ansible-venv.fish 3.10 stable-2.10
```

and I'm ready to run `ansible-playbook` or `ansible-test` in my clean environment. And when I want to reinitialize the venv, I just have to remove the venv directory.

The script is [here](https://gist.github.com/goneri/f7f3e371ad020c8651cb7af74d6b6aba) and depends on [FishShell](https://fishshell.com/), my favorite shell.

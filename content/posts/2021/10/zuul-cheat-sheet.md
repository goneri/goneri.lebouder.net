+++
title = "Zuul cheat sheet"
date = 2021-10-12T20:57:33+00:00
+++
My team at Ansible use [Zuul CI](https://zuul-ci.org/) to develop and release our collections. Time to time, I need to do some basic operation and I've started a cheat sheet. I'm sharing it since it may be helpful for someone else.

Abort a job:

```
$ zuul dequeue --tenant=ansible --pipeline=release --project=ansible-collections/ansible.utils --ref=refs/tags/2.4.2
```

Recreate a job job. In this case, we manually recreate a job in the release pipeline. This job was initially created by the push of a tag (--newrev).

```
$ zuul enqueue-ref --tenant=ansible --trigger=github --pipeline=release --project=ansible-collections/ansible.utils --ref=refs/tags/2.4.2 --newrev=6a0372849bec52672a74168b93b0677d2c6471fc
```

List all the ongoing nodepool request:

```
$ nodepool -s /etc/nodepool/secure.conf request-list
```

Kill a periodical job:

```
$ zuul dequeue --tenant=ansible --pipeline=periodic --project=ansible/ansible --ref refs/heads/stable-2.9
```

+++
title = "My Github workflow"
date = 2021-01-08T14:47:12+00:00
[taxonomies]
tags = ["git", "ansible"]
+++
The Ansible community uses Github to develop ansible-core and most of the Ansible Collections. The only exception I know is the Openstack's ansible-collection-openstack which uses a Gerrit ([ansible-collections-openstack](https://review.opendev.org/#/q/project:openstack/ansible-collections-openstack)).

So, as an Ansible developer, my normal day-to-day activities involve a lot of GitHub interactions. I review Pull Requests (PRs) and prepare new PRs all the time.

Before joining Ansible, I was working with [Gerrit](https://www.gerritcodereview.com/) which is a nice alternative solution to collaborate on a stream of patches.

In Gerrit, each patch from a branch is a PR. Every time we update a patch, its sha2 changes, and so Gerrit tracks them with a dedicated ID called [Change-id](https://gerrit-review.googlesource.com/Documentation/user-changeid.html). It looks like an extra line in the body of the commit message. e.g:

 Change-Id: Ic8aaa0728a43936cd4c6e1ed590e01ba8f0fbf5b

Gerrit provides a tool called git-review to pull and push the patches. When a contributor pushes a series of patches, each patch is correctly tracked by Gerrit and updates the right existing PR. This allows the contributor to reorganize the patches, change the order of series or import a patch from another branch.

With GitHub, a branch is a PR and most of the time, the projects prefer to use the branch to trace the iteration of the PR:

* my fancy feature
* fix: correct the test-suite
* fix: fix the fix
* fix: typo in previous commit
* bla

And this is fine, because most of the time, the branch will ultimately be squashed (one branch -\> one Git commit) during the final merge.

GitHub workflow is certainly more friendly for newcomers but it tends to be a source of complexity when you want to work on several PRs at the same time. For instance, I work on a new feature, but I also want to cherry-pick an experimental commit from a contributor. In this case I must remove this commit before I push my branch back on GitHub, or the extra commit will end-up in my feature branch.

Another example, if I'm working on a feature branch and find an issue with something unrelated, I need to switch to another branch to commit my fix and push it. This is cumbersome and often people just prefer to merge the fix in their feature branch which leads to confusion and questions during the code review.

To simplify, Gerrit allows better code modularity but also implies a better understanding of Git which is annoying when we try to attract new contributors. This is the reason why we use the current workflow.

To address the problem I wrote a script called push-patch (https://github.com/goneri/push-patch). I use it to push just my commits. For instance, I work on this branch:

* 1: doc: explain how to do something
* 2: typo: adjust a few details
* 3: a workaround for issue #19 that should not be merged

The first two commits are not directly related to the feature I'm implementing. And I would like to submit them immediately.

push-patch will allow me to only push the change 1 and 2 in two dedicated PR. Both branches will be based on main and can be merged independently.

```
$ push-patch 1
$ push-patch 2
```

Now, and that's the cool part [**😋**](https://getemoji.com/)! Let's imagine I want to push another revision of my first patch, I can use "git rebase -i" to adjust this commit and use push-patch again to use the updated patch.

```
$ vim foo
$ git add foo
$ git rebase --continue
$ ./push-patch 1
```

Internally push-patch uses git-notes to trace the remote branch of the patch. The Public-Branch field traces the name of the branch in my remote clone of the project and Pr-Url is the URL of the PR in the upstream project. e.g:

```
commit 1198db8807ebf9f4099598bcd41df25d465cbcae (HEAD -> main)Author: Gonéri Le Bouder <goneri@lebouder.net>Date:   Thu Jan 7 11:31:41 2021 -0500   elb_application_lb: enable the functional test       Remove the `unsupported` aliases for the `elb_application_lb` test.       Use HTTP instead of HTTPS to avoid the dependency on   `iam:ListServerCertificates` and the other Certificate related operations.Notes:   Public-Branch: elb_application_lb-enable-the-functional-test_24328       PR-Url: https://github.com/ansible-collections/community.aws/pull/348
```

This means that even if the patch content evolves, push-patch will still be able to continue to update the right PR.

In a nutshell, for each patch it will:

1. clone the project and switch on the main branch
2. read the patch notes
   1. if a branch name already exists it will use it, otherwise it will create a new one

3. switch to the branch
4. cherry-pick the patch
5. push the branch

push-patch expects just the sha2 of the commit to push. It also accepts a list of sha2. This is the reason why I often type thing like that:

**push-patch** $(**git** log -2 --pretty=tformat:%H)

The command passes to push-patch the SHA2 of the two last commits. It will push them in the two associated branches upstream. And at the end, I can use `git log`, or better [`tig`](https://github.com/jonas/tig), to get the URL of the Github review.

Right now, the command is a shell script and depends on the [hub](https://github.com/github/hub) command. I would like to rewrite it with a better programming language.

What about you? Do you also use some special tools to handle your PR?

+++
title = "How to grab Thunderbird 3.0.4 sources"
date = 2010-04-22T13:13:07+00:00
+++
Commit references commits can be found in the release note on the wiki: [https://wiki.mozilla.org/Releases/Thunderbird\_3.0.4](https://wiki.mozilla.org/Releases/Thunderbird_3.0.4)

```shell
hg clone -r b8e06312e645 http://hg.mozilla.org/releases/comm-1.9.1 thunderbird
cd thunderbird
echo 'ac_add_options --enable-application=mail' > .mozconfig
echo 'mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/objdir-tb-release' >> .mozconfig
hg clone -r ead1204d8b81 http://hg.mozilla.org/releases/mozilla-1.9.1 mozilla
```

Install the build dependencies ( [https://developer.mozilla.org/En/Simple\_Firefox\_build](https://developer.mozilla.org/En/Simple_Firefox_build) ).

Now we can launch the build

```
make -f client.mk
```

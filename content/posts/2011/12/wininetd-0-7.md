+++
title = "Wininetd 0.7"
date = 2011-12-04T22:29:25+00:00
+++

Just a reminder, this is the command line needed to build [WinInetd](http://www.xmailserver.org/wininetd.html) with gcc:

```shell
gcc service.c wininetd.c -lws2_32 -lm
```

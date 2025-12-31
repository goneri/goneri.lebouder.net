+++
title = "Allow broken certificate for a specific host with Python's requests"
date = 2025-09-17T21:03:40+00:00
+++
After a bit of trial error, this is how you can allow requests to connect to a specific host, despite a broken certificate:

```python
import requests
import requests.adapters
import ssl
import urllib3
from urllib3.util import create_urllib3_context

class AllowBrokenSSLContextHTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, **kwargs):
        ssl_context = create_urllib3_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=self.ssl_context,
        )

    def send(self, request, **kwargs):
        kwargs["verify"] = self.ssl_context.check_hostname
        return super().send(request, **kwargs)

session = requests.session()
session.mount(
    "https://wrong.host.badssl.com",
    AllowBrokenSSLContextHTTPAdapter(),
)
session.get("https://google.com")
session.get("https://wrong.host.badssl.com")
print("Can reach https://wrong.host.badssl.com despite the invalid hostname")
try:
    result = session.get("https://untrusted-root.badssl.com/")
except requests.exceptions.SSLError:
    print("fails has expected")
else:
    print("Ooops")
```

+++
title = "AWS: How to retrieve a KeyPair private key"
date = 2023-09-14T12:41:56+00:00
[taxonomies]
tags = ["tips", "cloud"]
+++
Note for myself, this is how you can download a copy of a KeyPair private key:

```
aws --region ca-central-1 ssm get-parameter --name /ec2/keypair/key-015b012fb114efc83 --with-decryption --query Parameter.Value --output text
```

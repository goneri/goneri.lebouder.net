+++
title = "Ansible and k8s: How to get the K8S_AUTH_API_KEY value?"
date = 2020-12-07T21:37:00+00:00
+++
The [community.kubernetes ](https://github.com/ansible-collections/community.kubernetes)collection accepts an `api_key` parameter that may sounds a bit confusing. It's actually the value of the token of a serviceaccount. It's actually an OAuth 2.0 (Bearer) token, it's associated with a user and a secret key. It's rather similar to what we can do with a login and a password.

[<img alt="" src="/wp-content/uploads/2020/12/luis.jpg" height="68" width="68" />](/wp-content/uploads/2020/12/luis.jpg)

In this example, we want to run our playbook as the k8sadmin user. We need to find the token associated with the user. The are actually looks for the a secret. You can list them this way:

```
[root@kind-vm ~]# kubectl -n kube-system get secret
NAME                                             TYPE                                  DATA   AGE
(...)
foobar                                           Opaque                                0      5h3m
foobar-token-w8lmt                               kubernetes.io/service-account-token   3      5h15m
foobar2-token-hpd6f                              kubernetes.io/service-account-token   3      5h9m
generic-garbage-collector-token-l7hvk            kubernetes.io/service-account-token   3      25h
horizontal-pod-autoscaler-token-sssg5            kubernetes.io/service-account-token   3      25h
job-controller-token-dnfds                       kubernetes.io/service-account-token   3      25h
k8sadmin-token-bklpd                             kubernetes.io/service-account-token   3      5h40m
(...)
```

The use the` -n` parameter to specific the `kube-system` namespace. Our system account is in the list, it's k8sadmin-token-bklpd. We can see the content of the token with this command:

```
[root@kind-vm ~]# kubectl -n kube-system describe secret k8sadmin-token-bklpd
Name:         k8sadmin-token-bklpd
Namespace:    kube-system
Labels:       <none>
Annotations:  kubernetes.io/service-account.name: k8sadmin
             kubernetes.io/service-account.uid: 412bf773-ca8e-4afa-a778-dac0f11b7807

Type:  kubernetes.io/service-account-token

Data
====
namespace:  11 bytes
token:      eyJhbGciO(...)2A
ca.crt:     1066 bytes

Here, you're done. The token is in the command output. You need now to pass its content to Ansible. Just keep in mind the token needs to remain secret. So it's a good idea to encrypt it with Ansible Vault.
You can use the K8S_AUTH_API_KEY environment variable to pass the token to the k8s_* modules:
```

$ K8S\_AUTH\_API\_KEY=eyJhbGciO(...)2A ansible-playbook my\_playbook.yaml

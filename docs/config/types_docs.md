
# More Rules #

## SSH ##

Add this to the /etc/snort/rules/local.rules..

```
alert tcp any any -> $HOME_NET 22 (msg: "[SSH-Auth]: ", sid: 1000002; rev: 1;) 

```

^ Now to test this, You will need to set up your own ssh,
and connect to it via some other machine..
 You can read these steps in 'docs/install/install_ssh.md'

If you got it right, (and figured out the ufw)
you should have seen something like:

```
04/29-08:13:08.602737  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22
04/29-08:13:09.544379  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22
04/29-08:13:09.662606  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22
04/29-08:13:09.669397  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22
04/29-08:13:09.669767  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22
04/29-08:13:09.670168  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22
04/29-08:13:09.670547  [**] [1:1000002:1] [SSH-Auth]:  [**] [Priority: 0] {TCP} 192.168.0.105:58056 -> 192.168.0.107:22


```


## Read The Logs ##

Since there was no instruction to 'decode' or 'decrypt' pcap/data.
All 'traffic' related topics have been met.





### End-Of-Doc ###

Next: Implement this  on a Django Project... "add-to-django.md"


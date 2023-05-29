# Bare Basic of Packet Capture #

### What we will cover ###

-> Reverse-Scanning
-> Target-Profile

### What we will cover ###

-> ssl/tls
-> Using 'flags'.. more


## Main ##

### SSL/Cert ###

By running nmap, we can see if a target is using port : 443...

this port is for ssl and tls... (Google that..)

So, if in fact they are using port:443..
then let's use sslscan, "brought to you by, Kali Linux"..

```
$ sslscan --show-certificate www.google.com:443

```

Some basic info here is :

```diff

  SSL/TLS Protocols:
SSLv2     disabled
SSLv3     disabled
TLSv1.0   enabled
TLSv1.1   enabled
TLSv1.2   enabled
TLSv1.3   enabled


```

^ This is at least a step in the right direction,
be we are still far from getting there..









## Main ##

### TargetScanning ###

Let's put every scanning option into a seperate file...

```scanners.py```

From here we can now have different scans:

-> nmap
-->> get_ports : 80, 8080, 8000, 443, 8443
-> sslscan
-->> get_protocols : SSL/TLS : SSLv2, SSLv3, TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3
-->> Signature Algorithm: sha256WithRSAEncryption
-> ip-api
-->> get_data : location, status, etc..







### The Wheel... ###

Since decrypting is a huge task, let's see who has already 
done it on our behaves..

well, none other than the masters..:

```
import pyshark

```


Don't worry, we still have our work cut out for us..

first, we need to filter the ```sslscan``` output,
(which is quite large), then we need to apply this to 
captured packets... 


But Wait! We need to first actually capture those packets..

Thus far, we have only been viewing them, and looking at the 
pretty streams of out put... (Not much use...)





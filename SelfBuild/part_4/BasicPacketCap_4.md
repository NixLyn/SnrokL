# Bare Basic of Packet Capture #

### What we will cover ###

-> Reverse-Scanning
-> Target-Profile



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


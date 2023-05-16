# Bare Basic of Packet Capture #

### What we will cover ###

-> Basics of Sockets
-> IPv4
-> TCP, UDP, ICMP
-> Decoding/Decryption
-> Saving Packets
-> Probing Target

## Basic Usage ##

$ tree
```
┌── de_confuse.py
├── File_man.py
├── listen_.py
└── packets/
    ├─ pcaps_0.txt
    └─ pcaps_1.txt
    └─ ...
└── targets/
    ├─ profile_0.txt
    └─ ...

```

To Run..

```
sudo python3 listen_.py

```

From here it will start pumping output...

## Purpose of Exercise ##

Hopefully, once all basics are covered
you should be able to modify these files
in order to:
A) Filter traffic:
A.1) Set Target
A.2) Traffic Type
A.3) Detect 'Scanners'

B) Save Captured Packets
B.1) Get encryption method of src IP (Using 'nmap')
B.2) Decrypt Packet by method

C) Counter Attack:
C.1) Get IP Location
C.2) HoneyPot Attacker


### Write Report ###



# Bare Basic of Packet Capture #

## Includes ##

-> File_Man:
-->> Self-Built Functins for handling filedata
-->> -> (Though pandas would probably work best..)

-> de_confuse:
-->> My sarcastic way of 'decoding' a packet
-->> after it has been restructured...

-> listener_0.py
-->> For this part, that is the ```main```

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
├── packets/
│    ├─ pcaps_0.txt
│    └─ pcaps_1.txt
│    └─ ...
└── targets/
    ├─ profile_0.txt
    └─ ...


```


To Run..

```
sudo python3 listen_.py

```

From here it will start pumping output...
(It will be messy..)

## Purpose of Exercise ##

A) To understand how to 'Sniff' a packet
B) How packets are structured
C) Learning the pain of decoding a packet..



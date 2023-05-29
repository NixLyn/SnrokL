# Part 1 #

```diff
It's dangerous to go alone...
...Take this with you:

```

# Bare Basic Packet Capture #

## Python Sockets ##




## Includes ##

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

A) To understand how to recvFrom a socket port.
B) How packets are structured.
C) Learning the pain of decoding a packet..



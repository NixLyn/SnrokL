# Bare Basic of Packet Capture #

### What we will cover ###

-> OOP
-> Importing the the Listener_
-> Using some basic 'filters'
-> Decoding packet data


## Main ##

To use this new tool we have built effectively,
we need to be able to import it in a seperate
script, run the tool with given parameters,
and utilize the data being processed..


in the ```main.py``` we will need to import the 
listener as such:

```
from listen_1 import Listen_ 

```

^x^ 

And yes, there are more effective ways to do this,
but for simplicity sake, and the point of this course,
we will be using vanilla methods...

### OOP... ###


We shall now __init__ the main-obj like so:

```
class Control_():
    def __init__(self, **kw):
        super(Control_, self).__init__(**kw)
        self.Li     = Listen_()

```

This way, we can utilize it in multiple ways..


### No Actual Args, yet ###

For this part we will prompt the user for which
IP to focus on.. 
(This technique can be used for Red&Blue)

But, first, we will need to make some changes to
the ```listener_2.py ```...

So let's add a parameter of 'target_ip'..

```
    def main(self, target_ip):
```


### Threads, No Needles ###

We Will Use threading, to seperate the processes..

```

    def main(self):
        try:
            print("[MAIN_STARTED]")
            # Prompt For Target..
            target_ip = input("[SELECT]-[TARGET]-[IP]:")

            # Run a thread, So we can still control the 'main' script..
            port_thread = threading.Thread(target=self.Li.main, args=(target_ip,))
            port_thread.start()

        except Exception as e:
            print("[E]:[MAIN]: ", str(e))
```


### Focus Only On ###

Now in the while loop, we will add on simple condition first..:
-> First, let's focus on IPv4.. (To keep it simple, for now)

```diff

        # ! IPv4_PACKET_SIZE -> 8
        if eth_proto == 8:
            print("[IPv4-/]")
            version, header_length, ttl, proto, src, target, data = self.ipv4_packet(data)
            if str(target_ip) in str(src):
                print(f"[FOUND]:[IPv4-Target]:[{src}]")
            else:
                continue


```

By doing so, the tool will now only print either:

-Somthing like:
```diff
***********************
[DEST_MAC]:[A4:B6:1E:FC:91:9C]
[SRC_MAC]:[84:4B:F5:01:42:93]
[ETH_]:[8]

[IPv4-/]


```
or 

```diff

***********************
[DEST_MAC]:[84:4B:F5:01:42:93]
[SRC_MAC]:[A4:B6:1E:FC:91:9C]
[ETH_]:[8]

[IPv4-/]
[FOUND]:[IPv4-Target]:[8.8.8.8]
         - [IPv4]:
    [VERSION]:[4]
    [HEADER_LEN]:[20]
    [TTL]:[116]
    [PROTO]:[1]
    [SRC]:[8.8.8.8]
    [TARGET]:[192.168.0.107]


        -- [DATA-HASHI]:: 

```



? now, if I'm not mistaken, this should work for both 
? coming and going data.. so we can see if our system is responding 
? to who-ever the target is..


### Looky-Here ###

What you might see on the output, be something like:

```diff


└─$ sudo python3 main.py
[MAIN_STARTED]
[SELECT]-[TARGET]-[IP]:8.8.8.8
[Targeting]:  8.8.8.8


```

-> Mind you this is google, and I don't know how they will feel
about the way we are doing this.. but since they are on Bug Crowd,
I'm assuming it's fine... I hope..


### Knock-Knock ###

.. Now in a diferent terminal, ``` ping 8.8.8.8 ```



## Still Cnfused..? ##

Yeah, you will realize, the output ```[HASHI]```s have only
been decoded via either utf-8, utf-16, or hex...


Next up.. More Confusion 🔭

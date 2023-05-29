
<style>
    .code_it {
        width: 80wv;
        right: 5vw; 
        height: fit-content;
        padding: 5px 80wv; 
        background-color: black; 
        color: #00ff00;
        border-radius: 20px;
    }



body {
	background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
	background-size: 400% 400%;
	animation: gradient 15s ease infinite;
	height: 100vh;
    width: 100vw;
}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

</style>


<body>




# My First Sock.. #

<div style="
width: 90wv;
height: 90wv;
padding-left: 10%; 
padding-right: 5%;
padding-top: 20px;
border-radius: 20px; 
background-color: #333333;
color: black;
">

## Server Side ##

### Concept ###

It wouldn't make much sense to try any 
make a phone call to someone who doesn't have a phone..

Same with sockets.. We first need an actual socket server
with which to connect to.

### Imports ###

luckily for us, socket should be pre-installed
(Cause it's actually needed for pip..)

So let's start:

_first_tcp_server.py_


<div class="code_it">

```python

import socket

```

</div>


[NOTE] : If you're used to vs-code / code-oss and have the relevant extensions, then you should see the suggestion pop-up..


### The Class ###

It is perceived that if you have been following allong in this series, that I need not explain the need for OOP...


### def __init__ ###

[__INIT__ :: # ? [SEG-01]](./another_folder/title.md#L20)

In the init function, we will define and configure our sockets..

For this particular example we will be using ```socket.socket(socket.AF_INET, socket.SOCK_STREAM)```.

_*AF_INET*_
-> This address family provides interprocess communication between processes that run on the same system or on different systems.

_*SOCK_STREAM*_
-> In the Internet domain, the SOCK_STREAM socket type is implemented on the Transmission Control Protocol/Internet Protocol (TCP/IP) protocol. A stream socket provides for the bidirectional, reliable, sequenced, and unduplicated flow of data without record boundaries.

[NOTE] :  So in a NutShell; we're saying we want to use TCP/IP..

For a "Client" to 'call', us we will need to 'registered' our "Number", 



<div class="code_it">

```python

self.ServSock   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
self.Host       = '127.0.0.1' 
self.Port       = 8000  # Google says to use port 80, but this is ok
self.ADDR       = (self.Host, self.Port)

```
</div>




### def main(self) ###

[__MAIN__ :: # ? [SEG-02]](./another_folder/title.md#L122)

In order to use this bag of socket codes as a _Server_, we must bind the socket.


<div class="code_it">

```python

self.sock.bind(('', self.port))

```
</div>


In my experience, you're not going to be heard if no-one is listening..

<div class="code_it">

```python

max_connections = 50
self.sock.listen(max_connections)

```
</div>



Surely, every "Company Building" has a 'front-door' ?
Our 'front-door' will be having an endless 'revolving door'..
Better know as a ```while true``` loop. Each visitor getting their
very own 'thread' which will handle the inbound and outbound traffic
between server and that 'visitor'. In order to achieve this __crochet__, we will need to:

<div class="code_it">

```python

import threading as thr
from thr import Thread as Thr


```

</div>


From here on, (within the ``` while True ``` Loop), we will be accepting out clients'
requests to connect to the server. To put it mordernly; "the clerk/secretary has now shown
our clients to the other room...

<div class="code_it">

```python

            try:
                conn, addr = self.sock.accept()
            except socket.error as e:
                print("[ERROR_CONNECTING_NEW_CLIENT] :", str(e))        
            try:
                new_thread = Thr(group=None, target=self.handle_client, args=(conn, addr))
                new_thread.start()
                self.threads.append(t1)
                self.th_count+=1
            except ThreadError as e:
                print(f'[ERROR]:[SERVER:~:MAIN]: {str(e)}')

```

</div>


...this other room being:




### def handle_clients(self, conn, addr) ###

[__HANDLE_CLIENT__ :: # ? [SEG-03]](./another_folder/title.md#L58)


To avoid the situation where you walk into a room, and it's like there's 
so many people talking over each other, so loudly, you couldn't possibly
order a cup off coffee.. We will use threading events.

First, we initiate it..

<div class="code_it">

```python

self.E = thr.Event()

```
</div>


Then in the next ``` while True: ```, we will first wait 
to recieve the length of a packet which is about to be sent..



<div class="code_it">

```python

data_len = int(conn.recv(64).decode())
if not data_len:
    self.E.wait()
if data_len > 0:
    new_data = str(conn.recv(data_len).decode())

```
</div>

By first sending the size, we can combat data corruptions and 
broken pipe errors. Which any online gamer will know, is a 
pain. But, TCP (unlike UDP) doesn't easily cause 'build-up' requests. 
But it does depend on what the goal is.. where online games have way 
too much data which become irrelevant very quickly, UDP is fine.
However, if you're making online transactions,, 
    ( well, you don't want any issues the: we got enough)


Once the client have secured a connection and the Client has sent the 
message_len & message_ (packet), the server can now process this data
and determine how to further handle the client.. So if eg. the client
has send "Hello Server!", we can then choose a response for the server
to send back to client, using the same technique/method that client used
to send the data..





### def reply(self, conn, data) ###

[__REPLY__ :: # ? [SEG-04]](./another_folder/title.md#L41)


Once it has been determined that the client's connection is following 
procedure, we can then reply.. So same as with the server side,
the client will first be expecting the length of the data, then the 
actual data.

<div class="code_it">

```python

msg_len = len(data)
send_len = str(msg_len).encode()
send_len += b' ' * (64 - len(send_len))
conn.send(send_len)
conn.send(data.encode())

```
</div>






### [FirstSocketServer](./example/first_tcp_server.py) ###


## Closing Word ##

Having this fundamental noted, we did not dive very deep, as this is 
to be an intermediate series.

### Next up ###

We will build the client side program, so we can say a proper 
"Hello Server!"


</div>

</div>
</body>
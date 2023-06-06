Basic Idea of the listener


```
# Will require SUDO, to run..

def listen(port):
    while True:
        conn = soc.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        raw_data, addr = this_con.recvfrom(port)
        print(f"[addr]:[{addr}]\n\t[raw_data]:[{raw_data}]\n----------\n")
```




# For visual purposes, I will be calling the server 
# a "Company Phone".. because,, well, because..


# ? [SEG-00]
# Let's 'declare' these libraries
import socket

# You can simplify the callbacks of 'imports as imp'
import threading as thr
from thr import Thread as Thr



# Every "Company needs a 'building'.." 
#   So let's use OOP, from the get-go..

# ? [Part 1-0-A]
class FirstSocketServer():
    # Hope you understand basics of OOP.. else: Google_is_friend == True
    # ? [SEG-01]
    def __init__(self, **kwargs):
        # explaination on the use of 'super' is outside the scope of this series
        super().__init__(**kwargs)
        # Let's declare to the 'socket' library what socket configuration we need
        self.ServSock   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # For eg purposes, we'll just be using 'localhost' -> 'Home Phone'
        self.Host       = '127.0.0.1' 
        # It is prefered to use standard ports for testing/debugging
        self.Port       = 8000  # Google says to use port 80, but this is ok
        # Host + Port = Address... 
        self.ADDR       = (self.Host, self.Port)

        # Let's add some needed variables:
        self.threads    = []
        self.th_count   = 0



    # ? [SEG-04]
    # Send_Method
    def reply(self, conn, data):
        try:
            msg_len = len(data)
            send_len = str(msg_len).encode()
            send_len += b' ' * (64 - len(send_len))
            print(f'[SENDING]:: {send_len}')
            print(f'[SENDING]:: {data}')
            conn.send(send_len)
            conn.send(data.encode())
            print("[MSG-SENT]")
            return
        except Exception as e:
            print('REPLY_ERROR:: ', str(e))


    # ? [SEG-03]
    # A new thread is made for each connection.. so the use os "self." will behave counterintuitive..
    def handle_client(self, conn, addr):
        try:
            client = []
            client = [conn, addr]
            # ! Feel free to print the 'conn', 
            # ! You might gain some xp on the topic :P
            print("[Client]:[CONNECTED]:", str(addr))
            # ? v v
            init_data = ""
            new_data = ""
            # ? ^ ^
            # ? Seriously don't have time to explain this logic..
            data_len = 0
            # ? Let's use 'Events' to keep the processing _lower-ish_
            self.E = thr.Event()
            # * You will find this is far simpler using -> AsyncIO.. 
            # * (But, that's for a different chapter)
        except Exception as e:
            print("[ERROR]:[SETTING_VARIABLES]: ", str(e))
        while connections == True:
            try:
                try: # GET IN_BOUND
                    data_len = int(conn.recv(64).decode())
                    if not data_len:
                        #print("WAITING_DATA_LEN:: ")
                        # ? Using FTP & Events, 
                        # ? we can hold the bus on this thread,
                        self.E.wait()
                        # ? untill we have recieved the expected 'packet'

                    if data_len > 0:
                        # Sometimes, network(s) has some issues,, so I do this (up to the dev..)
                        new_data = str(conn.recv(data_len).decode())
                        if not new_data:
                            self.E.wait()                                
                        else:
                            init_data = new_data
                            new_data = ''
                            #print("[IN_COMM]:data: ", str(data))
                except Exception as e:
                    print(f'[CLIENT_DISCONNECTED]: {addr} ')
                    print(f"[E]:[{str(e)}]")
                    if user:
                        self.th_count -= 1
                    return 
                    """
                    # Return will 
                    # ! NOT ! 
                    # kill the thread...
                    """
                try:
                    # ? Let's see if the 'Client' says "Hello Server!"... (Otherwise, that would be just rude.. ¿ )
                    if "Hello Server!" in new_data:
                        print("[Client is polite]")
                        self.reply(conn, "Hello Client!")
                except Exception as e:
                    print(f"[ERROR]:[Bad Greating..]:[{str(e)}]")
            except Exception as e:
                print("[ERROR_HANDLING_CLIENT]", str(e))


    # ? [SEG-02]
    # A Main.. as all good code should...
    def main(self):
        # Notice that we 'bind' with an empty 'host' value..
        try: # <- try/except is a great way to debug in a clean manner..
            self.sock.bind(('', self.port))
            print("[BINDING]")
        except Exception as e:
            print("[ERROR]:[NOT BINDING]: ", str(e))
            # ^ this is bad practice though.. we cover is future chapters
        try:
            # For a "Company Phone" to be accessible:
            #   it would need to be on 'Stand-By'
            max_connections = 50
            self.sock.listen(max_connections)
            # You can limit  ^  the total number of connections to the "Phone(s)"
            # If you choose to leave it blank, the default python socket
            #? max number of connections is ~65535~ 
            print(f"[LISTENING]:[{str(max_connections)}]")
        except Exception as e:
            print("[ERROR_LISTENING]", str(e))

        # A simple loop is all that's needed to keep the server 'program' running.. (Well, in the software part of it anyway, and if it doesn't crash, from people doing "WaterFallCoding".... 🌊)
        while True:
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



if __name__=="__main__":
    FSS     = FirstSocketServer()
    FSS.main()
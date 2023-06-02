#TODO::
#LOGIN/REGISTER         [DONE]:[STD]:
    # {NEXT}->{CROSS_ACCOUNT}
#CONTACT_LIST           [DONE]
#ADD_CONTACT            [DONE]
#CONTACT_STATUS         [DONE]
#MESSAGING              [NEXT]:[DIRECT_SEND if ONLINE]: 
    # {NEXT}->{SAVE_TILL_ONLINE}
#FORMS{DYNAMIC}         []
#MAPS                   []
#CALENDER               []
#CONNECT -> API         []
#SEARCH                 [?]


try:
    import socket
    import string
    import sys
    from threading import Thread, ThreadError
    import threading
    from File_man import File_Man
    from datetime import datetime
    
except Exception as e:
    print("[IPMORT]::[ERROR]:: ", str(e))

class server():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #IMPORTS
        self.FM = File_Man()

        #CONNECTIONS
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 8085
        self.addr = (self.host, self.port)

        #ACTIVE USERS
        self.LOGGED_IN = []


        # THREADS 
        self.threads = []

    #SEND_METHODE
    def reply(self, conn, data):
        try:
            msg_len = len(data)
            send_len = str(msg_len).encode()
            send_len += b' ' * (64 - len(send_len))
            #print(f'[SENDING]:: {send_len}')
            #print(f'[SENDING]:: {data}')
            conn.send(send_len)
            conn.send(data.encode())
            #print("[SENT]: ", str(data))
            return
        except Exception as e:
            print('REPLY_ERROR:: ', str(e))

    #CLEAN DATA - LIST-->>STR
    def lst_to_str(self, data_lst, delim):
        try:
            data_str = ""
            #print("LIST_TO_STR:: ", str(data_lst))
            if type(data_lst) == list:
                #print("CONVERTING")
                for _ in data_lst:
                    data_str += str(_)+str(delim)

                #print("LST_TO_STR", data_str)
            return data_str
        except Exception as e:
            print("LIST_TO_STR:[ERROR]:: ", str(e))

    #CLIENT_THREAD_HANDLE
    def handle_client(self, conn, addr):
        
        try:
            client = []
            client = [conn, addr]
            print("[Client]:[CONNECTED]:", str(addr))
            data = ""
            self.data = ""
            data_len = 0
            self.E = threading.Event()
        except Exception as e:
            print("[ERROR_SETTING_VARIABLES]: ", str(e))
        while True:
            try:
                try:
                    try: # GET IN_BOUND
                        data_len = int(conn.recv(64).decode())
                        if not data_len:
                            #print("WAITING_DATA_LEN:: ")
                            self.E.wait()
                        #print("[DATA_LEN]: ", str(data_len))
                        if data_len > 0:
                            #print("[WAITING]:>:[IN_COMM]")
                            self.data = str(conn.recv(data_len).decode())
                            if not self.data:
                                self.E.wait()                                
                            else:
                                data = self.data
                                #print("[IN_COMM]:self: ", str(self.data))
                                self.data = ''
                                #print("[IN_COMM]:data: ", str(data))

                        if "Hello" in data:
                            print("[HELLO]:->:[CLIENT]")
                            self.reply(conn, "Hello Client!")

                    except:
                        print(f'[CLIENT_DISCONNECTED]: {addr} ')
                        return

                except Exception as e:
                    print('CLIENT_HANDLE_ERROR: ', str(e))
                    return
            
            except Exception as e:
                print("[FAILED_TO_RECEIVE]: ", str(e))

            finally:
                data = ""
                data_len = 0
                self.data = ''

        print("[THREAD_EXITED]:",str(addr))
        return

    # THREAD CHECKER
    def check_and_join_threads(self):
        while True:
            for thread in self.threads:
                if isinstance(thread, threading.Thread) and thread.is_alive():
                    #print(str(thread), "IS_ACTIVE")
                    continue  # Thread is still active, skip it
                elif isinstance(thread, threading.Thread):
                    print(str(thread), "NOT_ACTIVE")
                    thread.join()  # Thread is no longer active, join it
                    self.threads.remove(thread)

    #MAIN_CLIENT_HANDLE
    def Main(self):
        #print("[STARTING_THREAD_CHECKER]")
        #threading.Thread(group=None, target=self.check_and_join_threads).start()


        #BIND_INCOMING_CONNECTION
        try:
            self.sock.bind(('', self.port))
            print("[BINDING] ")
        except Exception as e:
            print("NOT BINDING: ", str(e))
        #LISTEN
        try:
            # CAN CURRENTLY HANDLE 50 CLIENTS 
            self.sock.listen(50)
            print("[LISTENING]:")
        except Exception as e:
            print("[ERROR_LISTENING]", str(e))
        #CONNECTION THREADING_LOOP
        while True:
            try:
                conn, addr = self.sock.accept()
            except socket.error as e:
                print("[ERROR_CONNECTING_NEW_CLIENT] :", str(e))        
            try:
                t1 = threading.Thread(group=None, target=self.handle_client, args=(conn, addr))
                t1.start()
                self.threads.append(t1)
            except ThreadError as e:
                print(f'SERVER::MAIN:: {str(e)}')

if __name__=="__main__":
    s = server()
    s.Main()



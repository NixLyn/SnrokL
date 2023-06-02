#CONNECTION__
try:
    import socket
    import string
    from socket import error as sock_error
    import threading
    from threading import Thread, ThreadError
    from File_man import File_Man
    import time
except Exception as e:
    print("[IMPORT]::[ERROR]", str(e))

#CONNECTION CLASSES
class connections():
    #__INIT__
    def __init__(self, **kwargs):
        try:
            self.val = ""
            self.FM = File_Man()
        except Exception as e:
            print("[ERROR]::[SETTING]::{VARS}&&{IMPORTS}::", str(e))
            self.FM.write_file("ERRORS/CONNS.ffs", str(e), "*", "w")
            

    def close_conn(self):
        try:
            self.sock.close()
        except:
            print("[OOPs]")


    def start_conn(self, set_ip, set_port):
        try:
            print('[start_conn]..0')
            # '192.168.8.124'  #'192.168.1.100'  #'127.0.0.1'
            self.host =  set_ip             #'192.168.44.46'
            self.port =  set_port                   #80
            self.encap = "*"
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('[start_conn]..1')

        except Exception as e:
            print('CONNECTION_INIT[ERROR]:: ', str(e))
            #self.FM.write_file("ERRORS/CONNS.ffs", str(e), "*", "w")

        #SET SOCKET_CONNECTIONS
        try:
            print('[start_conn]..2')
            self.sock.connect((self.host, self.port))
            print("\n[CONNECTED]\n")
            #self.FM.write_file("CONN/CONN_STATE.txt", "PASSED*", "", "w")

        except Exception as e:
            print('SOCK_ERROR:: ', str(e))

        try:
            print("[CON_THREAD->>x]")
            self.con_threads()
        except Exception as e:
            print("[NO_CONNECTION]",str(e))

    def con_threads(self):
        try:
            print('[start_conn]..4')

            self.recv = threading.Thread(target=self.get_msg)
            self.watch = threading.Thread(target=self.send_msg)
            self.recv.start()
            self.watch.start()
            self.connected = True
            print("[THREADS_RUNNING]:[RECV]:[SEND]")

        except Exception as e:
            print("[NO_CONNECTION]")







    #RECEIVE
    def get_msg(self):
        print("[GET_MSG]:[RUNNING]")
        self.E = threading.Event()
        while True:
            data = ""
            try:
                data_len = int(self.sock.recv(64).decode())
                if not data_len:
                    self.E.wait()
                #print("DATA_LEN: ", str(data_len))
                if int(data_len) > 0:
                    data = str(self.sock.recv(data_len).decode())
                    if data:
                        print(f"[FROM-SERVER]: [{data}]")
                        #WRITE ALL INCOMING DATA TO IN_BOUND<FILE>
                        self.FM.write_file("IN_BOUND.txt", data, "*", "w")

                    data_len = 0
            except Exception as e:
                print("[SOCKET CLOSED]")
                print(str(e)) 
                self.sock.close()


    #TRANSMIT
    def send_msg(self):
        self.E = threading.Event()
        self.data = ""
        self.msg = ""

        self.tc = 0
        tc = 0
        self.test_conn = "TEST_CONN"+str(self.tc)

        print("[SEND_MSG]:[RUNNING]")
        path = "OUT_BOUND.txt"
        self.init_data = str(self.FM.read_file(path, "*"))
        try:
            while True:
                #UPDATE 
                try:
                    self.data = self.FM.read_file(path, "*")
                    if self.init_data != self.data and len(self.data) > 1:

                        toSend = ""
                        for _ in self.data:
                            toSend+=str(_)+"*"

                        msg_len = len(toSend)
                        send_len = str(msg_len).encode()
                        send_len += b' ' * (64 - len(send_len))
                        try:
                            self.sock.send(send_len)
                            self.sock.send(toSend.encode())
                            print("to_Send:: ", str(toSend))
                            #RESET DATA
                            self.init_data = self.data
                            toSend = ""
                        except Exception as e:
                            print("[ERROR]::SEND_MSG:TO_SERVER:", str(e))
                            time.sleep(10)

                except Exception as e:
                    print("[SEND_MSG]:[LOOP_ERROR] >", str(e))
                    break
        except Exception as e:
            print("SENDING_ERROR::", str(e))




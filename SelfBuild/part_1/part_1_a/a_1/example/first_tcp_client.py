# LOCAL IMPORTS
from File_man import File_Man
from conns  import connections

# REQUIRED IMPORTS
import socket
import threading as thr
from thr import Thread as Thr

class Client():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


    def close_conn(self):
        try:
            self.sock.close()
        except Exception as e:
            print(f"[ERROR]:[CLOSING_CONNECTION]")


    def start_conn(self, set_ip, set_port):
        # ? Config connection with given IP & Port
        try:
            self.host =  set_ip             #'127.0.0.1'
            self.port =  set_port           #80
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('[socket cofigured]')
        except Exception as e:
            print('[ERROR]:[NOT_CONFIGURED]: ', str(e))

        # ? Start Connection 
        try:
            print('[start_connection]')
            self.sock.connect((self.host, self.port))
            print("\n[CONNECTED]\n")
        except Exception as e:
            print('SOCK_ERROR:: ', str(e))
            self.FM.write_file("ERRORS/CONNS.ffs", str(e), "*", "w")

        # ? Call Function to start treads
        try:
            print("[CON_THREAD->>x]")
            self.con_threads()
        except Exception as e:
            print("[NO_CONNECTION]",str(e))

    def con_threads(self):
        try:
            print('[starting_threads]')
            self.recv = Thr(target=self.recv_msg)
            self.watch = Thr(target=self.send_msg)
            self.recv.start()
            self.watch.start()
            print("[threads_running]:[recv_msg]:[send_msg]")
        except Exception as e:
            print("[NO_CONNECTION]")





    #RECEIVE
    def get_msg(self):
        print("[GET_MSG]:[RUNNING]")
        self.E = thr.Event()
        while True:
            data = ""
            try:
                data_len = int(self.sock.recv(64).decode())
                if not data_len:
                    self.E.wait()
                if int(data_len) > 0:
                    data = str(self.sock.recv(data_len).decode())
                    if data:
                        #print("DATA RECVED:: ", str(data))

                        #WRITE ALL INCOMING DATA TO IN_BOUND<FILE>
                        self.FM.write_file("SOCKET_DATA/IN_BOUND.txt", data, "*", "w")
                        # LOG OFF
                        if "GOODBYE" in data:
                            print("LOGGED_OFF::", str(data))

                        # MESSAGING 
                        elif "MSG" in data:
                            #print("[MSG_IN]:", str(data))
                            if "SAVED" in data:
                                self.msg_of(data)
                            else:
                                self.stack_msgs(data)

                        #UPDATE CONTACTS LIST DATA
                        elif "STATE" in data:
                            #print("[GOT_TARGET_USER_STATE]::", str(data))
                            self.FM.write_file("CHATS/TARGET_STATE.txt", data, "*", "w")

                        # CONTACTS
                        elif "CONTS" in data:
                            c_list = data.split("$")
                            if "FAIL" in data:
                                # ("SOCKET_DATA/USER.txt", "*")
                                print("ADD_USER_FAIL", str(data))
                                #self.FM.write_file("CHATS/CONTS.txt", data, "%", "w")
                                self.FM.write_file("SOCKET_DATA/IN_BOUND.txt", "FAIL", "%", "w")

                            elif "EMPTY" not in c_list:
                                #print("C_LIST.. ", str(c_list[1]))
                                self.FM.write_file("CHATS/CONTS.txt", str(c_list[1]), "%", "w")
                                self.FM.write_file("SOCKET_DATA/OUT_BOUND.txt", "", "%", "w")
                            
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
        path = "SOCKET_DATA/OUT_BOUND.txt"
        msg_pat = "SOCKET_DATA/MSG_TO.txt"
        cont_path = "SOCKET_DATA/CONTS.txt"
        #CHECK OUT_BOUND<FILE> CHANGES
        try:
            self.init_msg = str(self.FM.read_file(msg_pat, ""))
            self.init_data = str(self.FM.read_file(path, "*"))
            self.init_conts = str(self.FM.read_file(cont_path, "*"))
            #print("INIT_DATA:: ", self.init_data)
        except:
            print("conns.py::send_msg():: ERROR??")
        try:
            while True:
                #UPDATE 
                try:

                    # PATHS
                    self.data = self.FM.read_file(path, "*")
                    self.msg = self.FM.read_file(msg_pat, "*")


                    # STANDARD
                    if self.init_data != self.data and len(self.data) > 1:
                        print(f"INIT: {self.init_data} :: DATA: {self.data} \n ")
                        tc+=1


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
                            print("[FUCKUP]::SEND_MSG:TO_SERVER:", str(e))
                            time.sleep(10)
                            break


                    # MSGS
                    if self.init_msg != self.msg and len(self.msg) > 0:
                        toSend = ""
                        for _ in self.msg:
                            toSend+=str(_)+"*"

                        msg_len = len(toSend)
                        send_len = str(msg_len).encode()
                        send_len += b' ' * (64 - len(send_len))
                        try:
                            self.sock.send(send_len)
                            self.sock.send(toSend.encode())
                            #print("toSend:: ", str(toSend))
                            #RESET DATA
                            self.init_msg = self.msg
                            #print(f"INIT_DATA ::\n>{self.init_data}\nN_DATA ::\n>{self.data}\n")
                            toSend = ""
                            #print("[MSG_SENT]:", str(toSend))
                        except Exception as e:
                            print("[FUCKUP]::SEND_MSG:TO_CONTACT:", str(e))
                            break

                except Exception as e:
                    print("[SEND_MSG]:[LOOP_ERROR] >", str(e))
                    break
        except Exception as e:
            print("SENDING_ERROR::", str(e))


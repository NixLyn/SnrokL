#CONNECTION__
try:
    import socket
    import string
    from socket import error as sock_error
    import threading
    from threading import Thread, ThreadError
    from file_handle import File_man
    import time
except Exception as e:
    print("[IMPORT]::[ERROR]", str(e))

#CONNECTION CLASSES
class connections():
    #__INIT__
    def __init__(self, **kwargs):
        try:
            self.val = ""
            self.FM = File_man()
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
            self.FM.write_file("ERRORS/CONNS.ffs", str(e), "*", "w")
            #self.FM.write_file("CONN/CONN_STATE.txt", "FAILED", "", "w")

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



    # FILTER MSG
    def msg_of(self, data):
        ls_data = []
        collected_ = []

        if "ACCESS_DENIED" in data:
            self.FM.write_file("SOCKET_DATA/MSG_OF.txt", data, "*", "w")

        if "SAVED" in data:
            ls_data = data.split("*")

            if len(ls_data) >= 6:
                user_ = str(ls_data[2])
                dt_stamp = str(ls_data[4])
                msg_of = str(ls_data[5])
                target_file = "MSGS/"+user_+".txt"
                to_save = dt_stamp+"*"+msg_of
                self.FM.write_file(target_file, msg_of, "&", "a")
                #print("[MSG]::", to_save, ":[SAVED]:", target_file)




    def stack_msgs(self, data):
        cont_ = ""
        file_name = ""
        collected_ = ""
        data_break = []
        buff_lst = []
        temp_msg = []
        shifted = []

        if "ACCESS_DENIED" in data:
            self.FM.write_file("SOCKET_DATA/MSG_OF.txt", data, "*", "w")

        if "MSGS_OF" in data:
            try:

                #print("[STACK_MSGS]:: ", str(data))
                data_break = data.split("@")
                #print("[DATA_BREAK][0]:", data_break[0])
                #print("[DATA_BREAK][1]:", data_break[1])

                if "*" in str(data_break[0]):
                    cont_ = str(str(data_break[0]).split("*")[1])

                if "$" in str(data_break[1]):
                     # CONVERT MSGS TO A LIST OF LISTS
                    msg_list = str(data_break[1]).split("$")
                    for i, val in enumerate(msg_list):
                        temp_msg = val.split("*")
                        if "INVITE" in str(temp_msg) or "MSGS_OF" in str(temp_msg) or len(temp_msg) < 4:
                            pass
                        else:
                            #print("TEMP_MSG:: ", str(temp_msg))
                            buff_lst.append(temp_msg)



                    
                    #for msg in buff_lst:
                    #    print("[STACK_ED]::", str(msg))



                    file_name = f"MSGS/{cont_}.txt"
                    self.FM.write_file(file_name, "", "$", "w")
                    self.FM.write_file(file_name, str(data_break[1]), "$", "w")

                # FOR TESTING ONLY
                #return buff_lst
                # ^^^^^^^^^^^^^^^^
            except Exception as e:
                print("[ERROR]::[STACK_MSGS]::",str(e))



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
                    self.conts = self.FM.read_file(cont_path, "*")


                    #if tc == self.tc:
                    #    print("TC",str(self.tc))
                    #    self.data = self.test_conn
                    #    self.tc+=1


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

                    # CONTACTS
                    if self.init_conts != self.conts and len(self.conts) > 1:
                        toSend = ""
                        for _ in self.conts:
                            toSend+=str(_)+"*"

                        msg_len = len(toSend)
                        send_len = str(msg_len).encode()
                        send_len += b' ' * (64 - len(send_len))
                        try:
                            self.sock.send(send_len)
                            self.sock.send(toSend.encode())
                            #RESET DATA
                            self.init_conts = self.conts
                            #print("[MSG_SENT]:", str(toSend))
                            toSend = ""
                        except Exception as e:
                            print("[FUCKUP]::SEND_MSG:TO_CONTACT:", str(e))
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




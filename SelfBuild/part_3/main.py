from listen_3 import Listen_ 
import threading
import subprocess



class Control_():
    def __init__(self, **kw):
        super(Control_, self).__init__(**kw)
        self.Li     = Listen_()
    

    def main(self):
        try:
            print("[MAIN_STARTED]")
            # Prompt For Target..
            ip_type = input('[IPv4]:or:[MAC]\n[4/6]')
            target_ip = input("[SELECT]-[TARGET]-[IP]:")


            # Let's map it :*
            ret_nmap = subprocess.getoutput(f"nmap --script ssh2-enum-algos {target_ip}")
            print("[This will messy...]: \n\n", ret_nmap)




            # Run a thread, So we can still control the 'main' script..
            port_thread = threading.Thread(target=self.Li.main, args=(target_ip, ip_type))
            port_thread.start()

        except Exception as e:
            print("[E]:[MAIN]: ", str(e))




if __name__=="__main__":
    Cont_ = Control_()
    Cont_.main()





from listen_2 import Listen_ 
import threading



class Control_():
    def __init__(self, **kw):
        super(Control_, self).__init__(**kw)
        self.Li     = Listen_()
    

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




if __name__=="__main__":
    Cont_ = Control_()
    Cont_.main()





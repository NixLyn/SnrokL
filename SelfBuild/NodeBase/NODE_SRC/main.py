from listen_1 import Listen_
from File_Man import File_man
import threading
from threading import Thread 


class Controller():
    def __init__(self, **kw):
        super(Controller, self).__init__(**kw)
        self.FM                 = File_man()
        self.Li                 = Listen_()


    def main(self):
        try:
            running = 0
            print('[WELCOME_SNROKLER] ')
            while True:
                print(f"[Running_Threads]: [{str(running)}]")
                file_name = input("[RULES_FILE_NAME]:")
                print(f"[USING]:[{str(file_name)}]")
                threading.Thread(target=self.Li.start_snrokl, args=(file_name, "LOCAL" )).start()
                running += 1
                print("[CHECK_DATA_FOLDER]\n")


        except Exception as e:
            print(f"[E]:[{str(e)}]")


if __name__=="__main__":
    C = Controller()
    C.main()

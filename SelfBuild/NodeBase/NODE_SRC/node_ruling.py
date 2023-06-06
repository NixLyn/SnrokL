from listen_1 import Listen_
from File_Man import File_man
import threading
from threading import Thread 


class Node_Ruling():
    def __init__(self, **kw):
        super(Node_Ruling, self).__init__(**kw)
        self.FM                 = File_man()
        self.Li                 = Listen_()


    def new_rules(self, cmd_):
        try:
            pass
        except Exception as e:
            print(f"[E]:[{str(e)}]")


    def collect_data(self, cmd_):
        try:
            pass
        except Exception as e:
            print(f"[E]:[{str(e)}]")


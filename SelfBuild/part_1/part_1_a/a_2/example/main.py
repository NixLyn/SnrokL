
from File_man import File_Man
from conns import connections


class ClientSide():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.FM     = File_Man()
        self.conn   = connections()



    def main(self):
        try:
            to_print = ""
            self.conn.start_conn("127.0.0.1", 8085)
            while True:
                to_send = input("[MSG-to-SERVER]: ")+"*"
                self.FM.write_file("OUT_BOUND.txt", to_send, "*", "w")
                to_getn = self.FM.read_file("IN_BOUND.txt", "*")
                for t in to_getn:
                    to_print += str(t)
                print(f"[SERVER-RESPONSE]: {to_print}")
        except Exception as e:
            print(f"[E]:[Main]:[{str(e)}]")




if __name__=="__main__":
    M = ClientSide()
    M.main()
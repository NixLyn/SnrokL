# BASE
import subprocess

# LOCAL
from File_man import File_Man
import time

# TODO:
    # ! CLEAN_DATA
    # ? TCP
    # ? UDP
    # ? SSH
    # ? FTP
    # ? SQL
    # ? SMTP/POP3
    # ? SSL/TLS
    # ? WEBMIN
    # ? etc

class NetMap():
    def __init__(self, **kw):
        super(NetMap, self).__init__(**kw)
        self.FM                 = File_Man()

    # FILTER - PORTS [PARAM]
    def get_param(self, data, param_):
        try:
            ret_data = []
            for index in data:
                if str(param_) in str(index):
                    print(f"[PARAM_]::[{str(index)}]")
                    ret_data.append(str(index))
            return ret_data
        except Exception as e:
            print(f"[E]:[GET_TCP]:[{str(e)}]")


    # FILTER - PORTS [TCP(s)]
    # ! ONLY_TCP
    def get_tcp(self, data_str):

        print("\n-- [FILTERING_NMAP_FOR_PORTS]")
        data = data_str.split(" ")
        try:
            print("\n-- -- [GETTING PORTS]")
            ret_data = []
            for index in data:
                if "/tcp" in str(index):
                    pudding = str(index.split("\n")[1])[:-4]
                    #print(f"[INDEX]::[{str(index)}]")
                    print(f"[*]:[PORT]::[{str(pudding)}]")
                    if str(pudding) not in str(ret_data):
                        ret_data.append(str(pudding))
            return ret_data
        except Exception as e:
            print(f"[E]:[GET_TCP]:[{str(e)}]")


    # ! BASH_SCRIPTED
    def og_scan(self, type_, host_, file_dir, flags_, params_):
        try:
            tcp_ = []
            to_save_ = ""
            if flags_:
                print(f"[FLAGS]:[{flags_}]")
            to_run      = "nmap -A "+flags_+" "+host_
            print(f"[RUNNING]:[> {to_run} <]")
            nmap_return = subprocess.getoutput(to_run)
            self.FM.save_scan(file_dir, f"nmap_scan_{type_}.csv", nmap_return)
            print("[NET_MAP]:[SAVED]")
            tcp_ = self.get_tcp(nmap_return)
            print("..[OG_SCAN-TCP_]:",str(tcp_))
            for p_ in tcp_:
                to_save_ += str(p_)+","

            print("[PORTS_TO_SAVE]:", to_save_)

            self.FM.write_file(file_dir+f"/nmap_ports_.csv", to_save_, "", "w")

            #self.FM.save_scan(file_dir, f"nmap_tcp_{type_}.csv", tcp_)
            print("[PORTS]:[SAVED]")
            #if params_:
            #    par_ = self.get_param(nmap_return, params_)
            #    self.FM.save_scan(file_dir, "nmap_paras.csv", nmap_return)
            #    print("[PARAMS]:[SAVED]")
            #    return par_
            #else:
            return to_save_
        except Exception as e:
            print(f"[E]:[OG_NMAP]:[>{str(e)}<]")


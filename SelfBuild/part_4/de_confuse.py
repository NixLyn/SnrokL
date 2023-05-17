# LOCAL
from File_man import File_Man


# SYS_BASE
import subprocess
from threading import Thread
import time
import socket
import struct
import textwrap
import codecs
#from pcapkit import extract, IP, HTTP



# ! MY_OWN_TSHARK
class DeFuse_():
    def __init__(self, **kw):
        super(DeFuse_, self).__init__(**kw)
        self.FM                 = File_Man()




    def from_x_hex(self, payload_):
        ret_ = ""
        try:
            byt_it = str(payload_).split(r"\x")
            d_sp = ""
            for it_ in byt_it:
                d_sp += str(it_)
            print(f"~~~~[HASHI_TESTING']\n\t[{d_sp}]")
#            return d_sp
            # ! ToDo: add "FromHex()"
            ret_ = d_sp
        except Exception as e:
            pass
            #print(f"\n\t ~~~~[E]:[FROM_xHEX_t0]:[{str(e)}]")


        try:
            # ? Decode...
            hashi_0 = payload_.decode('utf-16')
            print(f"\n\t ~~~~[HASHI_16]:[{hashi_0}]")
#            return hashi_0
            ret_ = hashi_0

        except Exception as e:
            pass
            #print(f"\n\t ~~~~[E]:[FROM_xHEX_t_01]:[{str(e)}]")

        try:
            # ? Decode...
            hashi_1 = codecs.decode(payload_)
            print(f"\n\t ~~~~[CODECS_]:[{hashi_1}]")
#            return hashi_0
            ret_ = hashi_1

        except Exception as e:
            pass
            #print(f"\n\t ~~~~[E]:[FROM_xHEX_t1]:[{str(e)}]")

        try:
            hashi_2 = payload_.decode('utf-8')
            print(f"\n\t ~~~~[HASHI_8]:[{hashi_2}]")
#            return hashi_2
            ret_ = hashi_2

        except Exception as e:
            pass
            #print(f"\n\t ~~~~[E]:[FROM_xHEX_t2]:[{str(e)}]")
        return ret_


    def to_sting(self, data_list):
        try:
            # Iterate through list:
            # Convert each hex to str
            # Append to ret_list
            pass
        except Exception as e:
            pass
            #print(f"\n\t ~~~~[E]:[To_String]:[{str(e)}]")






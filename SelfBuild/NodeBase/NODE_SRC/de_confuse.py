# LOCAL
from File_Man import File_man


# SYS_BASE
import subprocess
from threading import Thread
import time
import socket
import struct
import textwrap
import codecs


# TODO:
# ? Attempt '_ALL_' tools from:
# ?     -> codecs
# ?     -> cryptography
# ?     -> & more

# ! MY_OWN_DECODER-ish
class DeFuse_():
    def __init__(self, **kw):
        super(DeFuse_, self).__init__(**kw)
        self.FM                 = File_man()


    def from_x_hex(self, payload_, num_, file_name, mode_):
        try:
            
            dt_now = f"[CP-#]:[{str(grab_count)}]"+"%[DATE-TIME]:"+str(time.asctime())
            header_tag = f"#[DECODE]:|:[CP-#]:[{num_}]:|:[DT]:[{dt_now}]::"
            byt_it = str(payload_).split(r"\x")
            d_sp = ""
            for it_ in byt_it:
                d_sp += str(it_)


            met = ".split(r-'-\-x-') !(-)"
            f_sp = f"\n\t[METHOD]:[{str(met)}]\n\t[PAYLOAD]:[{str(payload_)}]\n\t[DECODE]:[{str(d_sp)}]"

            if "v" in mode_:
                print("\n\t ~~~~[HASHI_LISTIn']", str(d_sp))
            if "s" in mode_:
                self.FM.write_file("DATA/m1_"+file_name+"_decode.txt", f_sp, ";", "a+")
        except Exception as e:
            print(f"\n\t ~~~~[E]:[FROM_xHEX_t0]:[{str(e)}]")

        try:
            # ? Decode...
            hashi_0 = payload_.decode('utf-16')
            a_sp = f"#[DECODE]:[DT:[{dt_now}]::\n\t[METHOD]:[.decode('utf-16')]\n\t[CP-#]:[{num_}]\n\t[PAYLOAD]:[{payload_}]\n\t[DECODE]:[{hashi_0}]"
            if "v" in mode_:
                print(f"\n\t ~~~~[HASHI_16]:[{str(hashi_0)}]")

            if "s" in mode_:
                self.FM.write_file("DATA/m2_"+file_name+"_decode.txt", f_sp, ";", "a+")

        except Exception as e:
            print(f"\n\t ~~~~[E]:[FROM_xHEX_t_01]:[{str(e)}]")

        try:
            # ? Decode...
            hashi_1 = codecs.decode(payload_)
            b_sp = f"#[DECODE]:[DT:[{dt_now}]::\n\t[METHOD]:[codecs.decode(payload)]\n\t[CP-#]:[{num_}]\n\t[PAYLOAD]:[{payload_}]\n\t[DECODE]:[{hashi_1}]"
            if "v" in mode_:
                print(f"\n\t ~~~~[CODECS_]:[{str(hashi_1)}]")
            if "s" in mode_:
                self.FM.write_file("DATA/m3_"+file_name+"_decode.txt", b_sp, ";", "a+")

        except Exception as e:
            print(f"\n\t ~~~~[E]:[FROM_xHEX_t1]:[{str(e)}]")

        try:
            hashi_2 = payload_.decode('utf-8')
            if "v" in mode_:
                print(f"\n\t ~~~~[HASHI_8]:[{str(hashi_2)}]")
            c_sp = f"#[DECODE]:[DT:[{dt_now}]::\n\t[METHOD]:[.decode('utf-8')]\n\t[CP-#]:[{num_}]\n\t[PAYLOAD]:[{payload_}]\n\t[DECODE]:[{hashi_2}]"
            if "v" in mode_:
                print(f"\n\t ~~~~[CODECS_]:[{str(hashi_2)}]")
            if "s" in mode_:
                self.FM.write_file("DATA/m3_"+file_name+"_decode.txt", c_sp, ";", "a+")

        except Exception as e:
            print(f"\n\t ~~~~[E]:[FROM_xHEX_t2]:[{str(e)}]")








"""
import codecs as cs
cs.BOM
cs.BOM32_BE
cs.BOM32_LE
cs.BOM64_BE
cs.BOM64_LE
cs.BOM_BE
cs.BOM_LE
cs.BOM_UTF16
cs.BOM_UTF16_BE
cs.BOM_UTF16_LE
cs.BOM_UTF32
cs.BOM_UTF32_BE
cs.BOM_UTF32_LE
cs.BOM_UTF8
cs.BufferedIncrementalDecoder(
cs.BufferedIncrementalEncoder(
cs.Codec()
cs.CodecInfo(
cs.EncodedFile(
cs.IncrementalDecoder(
cs.IncrementalEncoder(
cs.StreamReader(
cs.StreamReaderWriter(
cs.StreamRecoder(
cs.StreamWriter(
cs.ascii_decode(
cs.ascii_encode(
cs.backslashreplace_errors(
cs.builtins
cs.charmap_build(
cs.charmap_decode(
cs.charmap_encode(
cs.decode(
cs.encode(
cs.escape_decode(
cs.escape_encode(
cs.getdecoder(
cs.getencoder(
cs.getincrementaldecoder(
cs.getincrementalencoder(
cs.getreader(
cs.getwriter(
cs.ignore_errors(
cs.iterdecode(
cs.iterencode(
cs.latin_1_decode(
cs.latin_1_encode(
cs.lookup(
cs.lookup_error(
cs.make_encoding_map(
cs.make_identity_dict(
cs.namereplace_errors(
cs.open(
cs.raw_unicode_escape_decode(
cs.raw_unicode_escape_encode(
cs.readbuffer_encode(
cs.register(
cs.register_error(
cs.replace_errors(
cs.strict_errors(
cs.sys
cs.unicode_escape_decode(
cs.unicode_escape_encode(
cs.unregister(
cs.utf_16_be_decode(
cs.utf_16_be_encode(
cs.utf_16_decode(
cs.utf_16_encode(
cs.utf_16_ex_decode(
cs.utf_16_le_decode(
cs.utf_16_le_encode(
cs.utf_32_be_decode(
cs.utf_32_be_encode(
cs.utf_32_decode(
cs.utf_32_encode(
cs.utf_32_ex_decode(
cs.utf_32_le_decode(
cs.utf_32_le_encode(
cs.utf_7_decode(
cs.utf_7_encode(
cs.utf_8_decode(
cs.utf_8_encode(
cs.xmlcharrefreplace_errors(
"""






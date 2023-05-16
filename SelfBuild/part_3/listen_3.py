# LOCAL
from File_man import File_Man
from de_confuse import DeFuse_

# SYS_BASE
import subprocess
from threading import Thread
import time
import socket
import struct
import textwrap

#from pcapkit import extract, IP, HTTP
#from cryptography.fernet import Fernet



# ! MY_OWN_TSHARK
class Listen_():
    def __init__(self, **kw):
        super(Listen_, self).__init__(**kw)
        self.FM                 = File_Man()
        self.DF                 = DeFuse_()

                    # v Add the Target_IP param
    def main(self, target_ip, ip_type):
        try:
            print("[Targeting]: ", str(target_ip))
            conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

            while True:
                raw_data, addr = conn.recvfrom(65536)
                dest_mac, src_mac, eth_proto, data = self.eth0_frame(raw_data)
                

                print(f"\n***********************\n[DEST_MAC]:[{str(dest_mac)}]\n[SRC_MAC]:[{str(src_mac)}]\n[ETH_]:[{str(eth_proto)}]\n")
                # ?  #wrong# -> print(f"\n[DATA]:[{str(self.ipv4_packet(data))}]")
                if ip_type == "6":
                    if str(target_ip) in str(dest_mac):
                        print(f"[OUTGOING]:[MAC]:[{str(dest_mac)}]: ")

                    if str(target_ip) in str(src_mac):
                        print(f"[INCOMING]:[MAC]:[{str(src_mac)}]: ")

                # ! IPv4_PACKET_SIZE -> 8
                if eth_proto == 8:
                    print("[IPv4-/]")
                    version, header_length, ttl, proto, src, target, data = self.ipv4_packet(data)
                    if ip_type == "4":
                        if str(target_ip) in str(src):
                            print(f"[FOUND]:[IPv4-Target]:[{src}]")
                        else:
                            continue
                    print(f"\t - [IPv4]:\n    [VERSION]:[{version}]\n    [HEADER_LEN]:[{header_length}]\n    [TTL]:[{ttl}]\n    [PROTO]:[{proto}]\n    [SRC]:[{src}]\n    [TARGET]:[{target}]")
                    print("\n\n\t-- [DATA-HASHI]:: \n")
                    self.DF.from_x_hex(data)

                    # ! ICMP
                    if proto == 1:
                        print("\t - [ICMP]:")
                        icmp_type, code, checksum, data = self.icmp_packet(data)
                        print(f"\t\t[ICMP_TYPE]:[{icmp_type}]")
                        print(f"\t\t[CODE]:[{code}]")
                        print(f"\t\t[CHECK_SUM]:[{checksum}]")
                       # print(f"\t\t\t[{target}]:[DATA]:[{str(data)}]")
                        print("\n\n\t-- [DATA-HASHI]:: \n")
                        self.DF.from_x_hex(data)



                    # ! TCP
                    if proto == 6:
                        print("[TCP]:")
                        src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = self.tcp_segment(data)
                        print(f"\t[SRC_PORT]:[{src_port}] :: [DEST_PORT]:[{dest_port}]")
                        print(f"\t[SEQUENCE]:[{seq}] :: [ACK_]:[{ack}]")
                        print(f"\t[FLAGS]:")
                        print(f"\t\t[URG]:[{flag_urg}]\n\t\t[ACK]:[{flag_ack}]\n\t\t[PSH]:[{flag_psh}]\n\t\t[RST]:[{flag_rst}]\n\t\t[SYN]:[{flag_syn}]\n\t\t[FIN]:[{flag_fin}]")
                        #print(f"\t\t\t[{target}]:[DATA]:[{str(data)}]")
                        print("\n\n\t-- [DATA-HASHI]:: \n")
                        self.DF.from_x_hex(data)
                    
                    # ! UDP
                    if proto == 17:
                        print("[UDP]:")
                        src_port, dest_port, length, data = self.udp_segment(data)
                        print(f"\t[SRC_PORT]:[{src_port}]\n\t[DEST_PORT]:[{dest_port}]\n\t[LEN][{length}]")
                        #print(f"\t\t[{target}]:[DATA]:[{data}]")
                        print("\n\n\t-- [DATA-HASHI]:: \n")
                        self.DF.from_x_hex(data)

                    # ! OTHER
                    else:
                        data_ = self.format_multi_line("\t\t", data)
                        #print(f"[{target}]:[OTHER]:[DATA]:[{data_}]")


                # ! OTHER - OTHER
                else:
                    data_ = self.format_multi_line("\t\t", data)
                    #print(f"[{target}]:[DATA]:[{data_}]")
                    self.DF.from_x_hex(data)




        except Exception as e:
            print(f"[E]:[LISTEN_]:[MAIN]:[{str(e)}]")

    # ? Unpack ethernet frame
    def eth0_frame(self, data):
        try:
            dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
            return self.get_mac_addr(dest_mac), self.get_mac_addr(src_mac), socket.htons(proto), data[14:]
        except Exception as e:
            print(f"[E]:[LISTEN_]:[ETH_0]:[{str(e)}]")

    # ? return properly formatted MAC addr
    def get_mac_addr(self, byte_addr):
        try:
            bytes_str = map('{:02x}'.format, byte_addr)
            return ':'.join(bytes_str).upper()
        except Exception as e:
            print(f"[E]:[LISTEN_]:[GET_MAC_ADDR]:[{str(e)}]")

    # ? CLEAN_FORMATTED IP_V4 ADDR
    def ipv4_(self, addr):
        try:
            return '.'.join(map(str, addr))
        except Exception as e:
            print(f"[E]:[LISTEN_]:[IPv4]:[{str(e)}]")

    # ? UNPACK IP_V4 PACKET
    def ipv4_packet(self, data):
        try:
            version_header_length   = data[0]
            version                 = version_header_length >> 4
            header_length           = (version_header_length & 15) * 4
            ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
            return version, header_length, ttl, proto, self.ipv4_(src), self.ipv4_(target), data[header_length:]
        except Exception as e:
            print(f"[E]:[LISTEN_]:[IPv4_PACKET]:[{str(e)}]")

    # ? UNPACK ICMP_DATA
    def icmp_packet(self, data):
        try:
            icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
            return icmp_type, code, checksum, data[4:]
        except Exception as e:
            print(f"[E]:[LISTEN_]:[ICMP_PACKET]:[{str(e)}]")

    # ? UNPACK TCP_DATA
    def tcp_segment(self, data):
        try:
            (src_port, dest_port, seq, ack, offset_resv_flag)   = struct.unpack('!HHLLH', data[:14])
            offset                                              = (offset_resv_flag >> 12) * 4
            flag_urg                                            = (offset_resv_flag & 32) >> 5
            flag_ack                                            = (offset_resv_flag & 16) >> 4
            flag_psh                                            = (offset_resv_flag & 8) >> 3
            flag_rst                                            = (offset_resv_flag & 4) >> 2
            flag_syn                                            = (offset_resv_flag & 2) >> 1
            flag_fin                                            = offset_resv_flag & 1

            return src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]
        except Exception as e:
            print(f"[E]:[LISTEN_]:[TCP_SEGMENT]:[{str(e)}]")

    # ? UNPACK UDP SEGMENT
    def udp_segment(self, data):
        try:
            src_port, dest_port, size = struct.unpack('!HH2xH', data[:8])
            return src_port, dest_port, size, data[8:]
        except Exception as e:
            print(f"[E]:[LISTEN_]:[UDP_SEGMENT]:[{str(e)}]")

    # ? BREAKS UP MULTI_LINE_PACKETS
    def format_multi_line(self, prefix, string, size=80):
        try:
            size -= len(prefix)
            if isinstance(string, bytes):
                string = ''.join(r'\x{:02x}'.format(byte) for byte in string) 
                if size % 2:
                    size -= 1
            return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])
        except Exception as e:
            print(f"[E]:[LISTEN_]:[FORMAT_MULTI_LINE]:[{str(e)}]")

if __name__=="__main__":
    L = Listen_()
    L.main()



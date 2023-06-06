# LOCAL
from File_Man import File_man
from de_confuse import DeFuse_

# SYS_BASE
import subprocess
from threading import Thread
import time
import socket
import struct
import textwrap


# ! Handle Packet by Port
class PortFig():
    def __init__(self, **kw):
        super(PortFig, self).__init__(**kw)
        self.FM                 = File_man()
        self.DF                 = DeFuse_()


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

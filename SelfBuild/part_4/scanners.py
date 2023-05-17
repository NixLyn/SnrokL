import os
import sys
import subprocess



class Scanners_():
    def __init__(self, **kw):
        super(Scanners_, self).__init__(**kw)
        pass




    def net_map(self, target_ip):
        try:
            # nmap-.. :*
            print(f"-> $ nmap -A -sC -sV -Pn {target_ip}")
            ret_nmap = subprocess.getoutput(f"nmap -A -sC -sV -Pn {target_ip}")
            print("[bland-nmap...]: \n\n", ret_nmap)
        except Exception as e:
            print(f"[E]:[net_map]:[Scanners_]:[{str(e)}]")

    def get_ports(self, target_ip):
        try:
            # nmap-.. :*
            print(f"-> $ nmap -A -sC -sV -Pn {target_ip}")
            ret_nmap = subprocess.getoutput(f"nmap -A -sC -sV -Pn {target_ip}")
            print("[bland-nmap...]: \n\n", ret_nmap)
        except Exception as e:
            print(f"[E]:[net_map]:[Scanners_]:[{str(e)}]")







            # nmap-.. :*
            #ret_nmap = subprocess.getoutput(f"nmap --script ssh2-enum-algos {target_ip}")
            #print("[This will messy...]: \n\n", ret_nmap)


            # SSLSCAN.. :*
            #ret_ip_api = subprocess.getoutput(f"sslscan --show-certificate {target_ip}:443")
            #print("[This will messy...]: \n\n", ret_ip_api)

            # IP-API-lookup.. :*
            #ret_ip_api = subprocess.getoutput(f"curl http://ip-api.com/json/{target_ip}")
            #print("[This will messy...]: \n\n", ret_ip_api)


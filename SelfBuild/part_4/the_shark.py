import pyshark
import rsa

from File_man import File_Man
from de_confuse import DeFuse_


class DaShark_():
    def __init__(self, **kw):
        super(DaShark_, self).__init__(**kw)
        self.FM                 = File_Man()
        self.DF                 = DeFuse_()
    
    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False


    def take_this(self, target_ip, data, key):
        try:
            print(f"~[TARGET]:[{target_ip}]\n~[CIPHERED_TEXT]:[{data}]\n~[KEY]:[{key}]\n~~~~\n")
            try:
                text = self.decrypt(data, key)
                print(f"[PyShark-Decryption]: \n\n***\n {text} \n***\n")
            except:
                pass

            try:
                text = self.decrypt(self.DF.from_x_hex(data), key)
                print(f"[PyShark-Decryption]: \n\n***\n {text} \n***\n")
            except:
                pass


                # 9C:9D:2C:57:BE:FE:AD:8E:94:44:F1:38:67:C5:7D:D0:5E:B6:AC:98
            pass
        except Exception as e:
            print(f"[E]:[DaShark]:[TakeThis]:[{str(e)}]")
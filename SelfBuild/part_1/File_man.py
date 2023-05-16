#ToDo::
    #ENCRYPTION/DECRYPTION

import os
from pathlib import Path


class File_Man():
    def __init__(self, **kwargs):
        pass
 
    def check_prof_(self, f_name, i_):
        nf_name = ""
        ff_name = ""
        print(f"[PROF_NAME]:[{str(f_name)}]")
        print("[I_]:",str(i_))
        try:
            check_f = self.check_dir(f_name)
            if check_f == False:
                print("[NEW_PROFIILE]")
                return f_name
            else:
                print("[PROFIILE_EXISTS]")
                nf_name = f_name+"_"+str(i_)
                print(f"[TRYING]:[{nf_name}]")
                ch_dir = self.check_dir(nf_name)
                if ch_dir == False:
                    ret_ = nf_name
                    print("[RET_DIR]:", str(ret_))
                    return ret_
                else:
                    ff_name = self.check_prof_(nf_name, i_+1)
                    return ff_name
        except Exception as e:
            print(f"[E]:[CHECK_PROF_]:[{str(e)}]")

    def save_scan(self, f_dir_, scan_, scan_stack):
        try:
                        # ? Dir_For Profile
            dir_name_   = f_dir_+"/"
            # ? should check the dir tho...
                        # ? Scan_Name
            file_name_  = dir_name_ +scan_
            self.write_file(file_name_, scan_stack, "\n", "a+")
        except Exception as e:
            print(f"[E]:[SAVE_SCAN]:[>{str(e)}<]")

    def make_dir(self, path):
        os.mkdir(path)
        return 0

    def file_list(self, path):
        file_list = []
        file_list = os.listdir(path)
        return file_list

    def clean_data(self, data, delim):
        n_data = data[2:-2]
        n_list = n_data.split(str(delim))
        return n_list

    def read_file(self, file_name, delim):
        if file_name:
            try:
                with open(file_name, "r") as rf:
                    data = rf.readlines()
                    rf.close()
                    print("[FILE_READ]")
                    return (self.clean_data(str(data), delim))
            except Exception as e:
                print("ERROR_READING_FILE", str(e))
                return "ERROR_READING_FILE"


    # ! BOKEN
    def read_file_str(self, file_name):
        f_str = ""
        if file_name:
            try:
                with open(file_name, "r") as rf:
                    data = rf.readlines()
                    rf.close()
                return data
            except Exception as e:
                print("ERROR_READING_FILE", str(e))
                return "ERROR_READING_FILE"

    def write_file(self, file_name, data, delim, rwm):
        print(f"[FILE_NAME]:[IN_Q]:[{str(file_name)}]")
        if "[" in file_name or "]" in file_name:
            return
        text = ""
        fc = self.check_file(file_name)
        try:
            if fc == False:
                with open(file_name, "x") as wf:
                    wf.write(text)
                    wf.close()
                print(f"[FILE_MADE]\n    [>{str(file_name)}<]")
        except Exception as e:
            print(f'[E]:[CREATING_NEW_FILE]:[{str(e)}]')
            pass
        if file_name:
            # ? CHECK DATA TYPE
            if type(data) == str:
                text = data
            elif type(data) == list:
                for _ in data:
                    text += str(_) + str(delim)
            elif type(data) == str and len(data) == 0:
                text = ""
            # ? WRITE AS STR
            with open(file_name, rwm) as wf:
                wf.write(text)
                wf.close()
            return

    def check_file(self, file_name):
        path_to_file = file_name
        path = Path(path_to_file)
        if path.is_file():
            return True
        else:
            return False

    def check_dir(self, dir_name):
        path_to_file = dir_name
        path = Path(dir_name)
        try:
            if os.path.isdir(dir_name):
                return True
            else:
                return False
        except Exception as e:
            print(f'\n\n!![ERROR]!!\n[DIR_TEST]::[>{str(e)}<]')














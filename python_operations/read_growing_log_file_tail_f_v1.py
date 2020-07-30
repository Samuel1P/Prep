# This program will read a file which is constantly appended with new entries (ex. Log files)
# Assuming a log file is used which is adding new entries frequently
# Advantage of using this is we only read the newly added entry rather that reading the entire file. (Generators)
# There's not much real life use case, but it it good to know (asked in Dell EMC and Nutanix)
# A usecase could be, Notify if a certain text appears in the log entries. (we may use regex for that case after reading the line)

import os
import time


def tail(f_obj):
    f_obj.seek(0, os.SEEK_END)
    while True:
        rec = f_obj.readline()
        if not rec:
            time.sleep(2)
            continue
        yield rec


log_obj = open("growin_file.log", "r")
gen_method = tail(log_obj)
for line in gen_method:
    print(line)

# This program will read a file which is constantly appended with new entries (ex. Log files)
# Assuming a log file is used which is adding new entries frequently
# There's not much real life use case, but it it good to know (asked in Dell EMC and Nutanix)
# A usecase could be, Notify if a certain text appears in the log entries. (we may use regex for that case after reading the line)
import time
recent_pos = 0

while True:
    with open("growing_file.log", "r") as f_obj:
        f_obj.seek(recent_pos)
        unread_data = f_obj.read()
        recent_pos = f_obj.tell()
        if unread_data:
            print (unread_data)
        time.sleep(5)

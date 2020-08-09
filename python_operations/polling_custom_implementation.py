# We have built a custom polling module to call method until timeout is reached or Truthy value is returned;
# whichever reached first. The concatenate_string method fetches a random element from a list and checks it can be
# concatenated with a string. Return value is Boolean

import random
import time

value_ls = [1,2,3,4,4,7,8,6,7,4,3,"mystring"]
check_every = 2
timeout = 10

def poll(wait_time, start_time, time_out):
    time.sleep(wait_time)
    current_time = time.time()
    print (f"Checking again after {wait_time} seconds...")
    print (f"Total Elapsed time {(current_time - start_time):.2f}")
    if current_time - start_time >= time_out:
        print ("Could not find String in given time out.")
        return False
    return True

def concatenate_string(value):
    start_time = time.time()
    while True:
        try:
            v = random.choice(value)
            v = v + " concatenate this random string."
            return True
        except Exception as e:
            print ("Error : ", e)
            if not poll(check_every, start_time, timeout):
                return False

print ("Method Result = ", concatenate_string(value_ls))
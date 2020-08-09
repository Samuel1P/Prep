# In this program we demo dynamic wait using the polling module (a third party module).
# The concatenate_string method fetches a random element from a list and checks it can be concatenated with a string.
# Return value is Boolean
# https://medium.com/@justiniso/using-the-polling-module-in-python-87052d7da4d9
# https://github.com/justiniso/polling

import random
from polling import poll, TimeoutException


value_ls = [1,2,3,4,6,7,8,6,7,4,3,"mystring"]

def concatenate_string(value):
    while True:
        try:
            v = random.choice(value)
            v = v + " concatenate this random string."
            return True
        except Exception as e:
            print (e)
            return False
try:
    poll(lambda: concatenate_string(value_ls), step=2, timeout=10)
except TimeoutException as e:
    print("could not get the string bruh", e)

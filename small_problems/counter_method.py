# This is the most frequent program that is asked in all my python interviews.
# This can be easily done with Counter module in collections package.


s_ = "aaAAbbCcda"

def counter(s):
    counter_dict = {}
    for i in s:
        if i not in counter_dict:
            counter_dict[i]= 1
        else:
            counter_dict[i] += 1
    return counter_dict

print (counter(s_))
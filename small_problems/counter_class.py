# This is the most frequent program that is asked in all my python interviews.
# This program is using class
# This can be easily done with Counter module in collections package.


s_ = "aaAAbbCcda"

class CounterClass:
    def __init__(self, s):
        self.s = s
    def counter(self):
        counter_dict = {}
        for i in self.s:
            if i not in counter_dict:
                counter_dict[i]= 1
            else:
                counter_dict[i] += 1
        return counter_dict

count_obj = CounterClass(s_)
print (count_obj.counter())
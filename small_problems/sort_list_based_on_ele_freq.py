"""
This Program sorts the chars in a string based on the frequency of the chars and if the frequency is same,
it adds another constraint which sorts based on chars lexicographic rank
"""
from collections import Counter

my_list = 'bbbbbdddddkkssooaaaaaqqqaaBBBBBa'

count_dict = Counter(my_list)
count_list = list(count_dict.items())
count_list.sort(key=lambda x: x[1])
print(count_list)  # Sort by frequency of chars
count_list.sort(key=lambda x: [x[1], x[0]])
print(count_list)  # If the char frequency is equal , sort lexicographically

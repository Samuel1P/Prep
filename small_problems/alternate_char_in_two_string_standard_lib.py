from itertools import zip_longest

i = '123'
j = 'xyz'

def alt(x,y):
    return "".join(a+b for a,b in zip_longest(x,y,fillvalue="^"))

print (alt(i,j))
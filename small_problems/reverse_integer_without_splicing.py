# This program reverse an integer without datatype conversion or splicing.

my_num = 321

def reverse(num):
    rev = 0
    while num > 0:
        buf = num % 10
        rev = (rev * 10) + buf
        num = num // 10
    return rev

print (reverse(my_num))
# sum of all the individual digits in an integer

def sum_digits(num):
    out = 0
    while num > 0:
        dig = num % 10
        out = out + dig
        num = num // 10
    return out

print (sum_digits(5546))
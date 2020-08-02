# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# Fibonacci numbers for the first 15 integers from 0

s = 15
fibo = [0,1]

for i in range(0, s+1):
    fibo.append(fibo[-2] + fibo[-1])

print (fibo)



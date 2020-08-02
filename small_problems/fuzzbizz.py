#if int is divisible by both 3 and 5, then print fizzbuzz
#if int is divisible by only 5, then print buzz
#if int is divisible by only 3, then print fizz
# if int is not divisible by both print the int

for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    else:
        print(fizzbuzz)

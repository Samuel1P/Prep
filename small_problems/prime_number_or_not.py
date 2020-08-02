# List of first few 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71.
# https://www.tutorialsteacher.com/python/python-else-loop
# https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
# this is python specific

def prime_or_not(num):
    if num > 1:
        print(num)
        print (list(range(2, num)))
        for i in range(2, num):
            print (num, i)
            if num % i == 0:
                print ("not prime")
                break
        else:
            print ("prime")
    else:
        print ("not")

prime_or_not(2)
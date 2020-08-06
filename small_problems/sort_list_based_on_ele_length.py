# Pythonic Way
my_list = ['aaa','bcd','cd','def','pqwdwe','k', 'ab', 'ba','ab']
my_list.sort(key=len, reverse=False)  # sorts the elements based on length of each element in  ascending order
print(my_list)
my_list.sort(key=len, reverse=True)  # reverses the position of list
print (my_list)
my_list.sort()  # For a alphaneumeric sort
print (my_list)

"""
# Algorithmic way
my_list = ['aaa','bcd','cd','a','def','pqwdwe','k', 'ab', 'ba','ab','a']

def quick_sort(arr):
    if len(arr) < 2 :
        return arr
    pivot = arr[-1]
    low = []
    high = []
    mid = []
    for i in arr:
        if len(i) > len(pivot):
            high.append(i)
        elif len(i) < len(pivot):
            low.append(i)
        elif len(i) == len(pivot):
            mid.append(i)
    return quick_sort(low) + mid + quick_sort(high)

print (quick_sort(my_list))

def bub_sort(arr):
    size = len(arr)
    count = 0
    for ind in range(0, size-1):
        sz = len(arr[ind])
        sz1 = len( arr[ind+1])
        if sz > sz1:
            arr[ind], arr[ind+1] = arr[ind+1], arr[ind]
            count = count +1
    if count == 0:
        return arr
    else:
        return bub_sort(arr)

print (bub_sort(my_list))

"""

#Easy and best way to sort integers in a list
#https://www.youtube.com/watch?v=kFeXwkgnQ9U

arr_ = [3,1,4,5,3,6,7,3,2,1]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    high = []
    low = []
    dup = []
    for ele in arr:
        if ele > pivot:
            high.append(ele)
        elif ele < pivot:
            low.append(ele)
        elif ele == pivot:
            dup.append(ele)
    return quick_sort(low)+dup+quick_sort(high)

print (quick_sort(arr_))
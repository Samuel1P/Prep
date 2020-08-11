arr_ = [1,3,4,9,3,4,33,45,5]

def rev(arr):
    size = len(arr)
    out = []
    for index in range(size-1, -1, -1):
        out.append(arr[index])
    return out


print (rev(arr_))
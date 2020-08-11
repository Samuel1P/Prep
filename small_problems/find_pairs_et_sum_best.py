arr_ = [1,3,4,9,3,4,33,45,5]
tot_ = 12

def boom(arr, sum):
    arr.sort()
    left = 0
    right = len(arr)-1
    pairs = []
    unpair1 = []
    unpair2 = []
    while (left <= right):
        if arr[left]+arr[right] > sum:
            unpair1.append((arr[left], arr[right]))
            right = right-1

        elif arr[left]+arr[right] < sum:
            unpair2.append((arr[left], arr[right]))

            left = left + 1
        elif arr[left]+arr[right] == sum:
            pairs.append((arr[left], arr[right]))
            left = left+1
            right = right-1
    print (unpair1)
    print(unpair2)
    return pairs


print(boom(arr_, tot_))
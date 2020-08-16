arr_ = [1,3,4,9,3,4,33,8,45,5]
tot_ = 12

def boom(arr, sum):
    arr.sort()
    left = 0
    right = len(arr)-1
    pairs = []
    while (left <= right):
        if arr[left]+arr[right] > sum:
            right = right-1
        elif arr[left]+arr[right] < sum:
            left = left + 1
        elif arr[left]+arr[right] == sum:
            pairs.append((arr[left], arr[right]))
            left = left+1
            right = right-1
    return pairs


print(boom(arr_, tot_))
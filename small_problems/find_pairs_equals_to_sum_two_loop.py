arr_ = [1,9,2,4,5,6,7,6,6,8,11]
tot_ = 12

def find_pair(arr, tot):
    size = len(arr)
    pair_list = []
    for i in range(size):
        for j in range(i+1,size):
            if arr[i]+arr[j] == tot:
                pair_list.append((arr[i],arr[j]))
    return pair_list


print (find_pair(arr_, tot_))
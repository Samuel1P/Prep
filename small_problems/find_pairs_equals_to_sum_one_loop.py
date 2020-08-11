arr_ = [1,9,2,4,5,6,7,6,6,8,11]
tot_ = 12

def find_pair(arr, tot):
    ref_list = []
    pair_list = []
    for num in arr:
        if tot - num in ref_list:
            pair_list.append((tot-num, num))
        else:
            ref_list.append(num)
    return pair_list

print (find_pair(arr_, tot_))
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]



def common(arr1, arr2):
    ref_dic = {i: 1 for i in arr1}
    common_ele = []
    for i in arr2:
        if ref_dic.get(i) != None:
            common_ele.append(i)
    return common_ele

print (common(l1, l2))
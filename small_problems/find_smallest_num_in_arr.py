l1 = [3,4,5,6,7,1,2,3,4,5]

max = l1[0]
for i in range(len(l1)):
    if l1[i] > max:
        max = l1[i]

print (max)
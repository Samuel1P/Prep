s = "aaAAbbCcda"
counter = {i: s.count(i) for i in set(s)}
print (counter)
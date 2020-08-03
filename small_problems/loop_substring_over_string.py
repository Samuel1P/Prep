def count_substring(string, sub_string):
    count = 0
    subs = len(sub_string)
    for item in range(len(string)-subs+1):
        c = string[item:subs+item]
        print (c)
        if sub_string == c:
            count = count + 1
    return count

print (count_substring("abcdefg", "is"))
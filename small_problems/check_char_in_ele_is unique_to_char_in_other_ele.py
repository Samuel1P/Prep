# Asked in Tekion Interview

example_1 = "get bad oor" # should output unique
example_2 = "water heater" # should output not unique  ( because - a, e, r)
example_3 = "aaaa bbbb cccc" # unique
example_4 = "aaaa bbbb ca"  # not unique ( because - a is shared in first and last word)
example_5 = "aaa bbb bbb" # not unique ( because - b is shared in 2nd and last word)

def helper(my_str):
    my_ls = my_str.split()
    for i in range(0, len(my_ls)):
        parse = (my_ls[i], "".join(my_ls[i+1:]))
        yield parse

def match(gen):
    for x in gen:
        for i in x[0]:
            if i in x[1]:
                return "NOT UNIQUE"
    else:
        return "UNIQUE"

print (match(helper(example_5)))




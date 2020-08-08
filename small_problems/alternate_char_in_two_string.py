x = '123'
y = 'xyz'

def alt(a, b):
    if not a:
        return b
    elif not b:
        return a
    else:
        return a[0]+b[0]+ alt(a[1:],b[1:])

print (alt(x,y))
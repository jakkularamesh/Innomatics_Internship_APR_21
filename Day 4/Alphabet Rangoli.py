def print_rangoli(size):
    a='abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        temp = '-'.join(a[size-1:abs(i):-1]+a[abs(i):size])
        print(temp.center(4*size-3,'-'))
        


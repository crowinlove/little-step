lst = list((map(int,input().split())))
if 10 in lst:
    if lst.index(10)<20:
        print(lst.index(10)+1)
    else:
        print(0)
else:
    print(0)
        
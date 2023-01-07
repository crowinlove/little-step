list = [1]
for i in range(10):
    #打印每一行
    for k in range(32-3*i):
        print(' ',end ="")
    print("1",end="")
    for p in range(1,len(list)):
        x = '{:>6}'.format(list[p])
        print(x,end = "")
    print()
    j = len(list)
    listgap = []
    for i in range(j-1):
        listgap.append(list[i]+list[i+1])
    listgap.append(1)
    listgap.insert(0,1)
    list = listgap
    
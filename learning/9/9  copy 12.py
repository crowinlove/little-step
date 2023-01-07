while True:
    n = input()
    m = n.split("5")
    while "" in m:
        m.remove('')
    lst = []
    for i in m:
        list(i)
        if i.count("0")  == len(i):
            lst.append(0)
        else:
            lst.append(int(i))
    lst.sort()
    for i in lst:
        print(int(i),end = " ")
        
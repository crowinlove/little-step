while True:
    n = input()
    m = n.split("5")
    if n.count("5") != len(n):
        for i in m:
            if "" in m:
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
    print()  
       
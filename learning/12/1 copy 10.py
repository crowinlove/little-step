while True:
    list1 = ["A","B","C","D","F"]
    list2 = [4,3,2,1,0]
    p = []
    a = dict(zip(list1,list2))
    shuru = list(input().split())
    for i in shuru:
        if i not in list1:
            p.append(i)
    if p == []:
        k =0.0
        for i in shuru:
            k+= float(a[i])
        t = int(len(shuru))
        print("%.2f" % (k/t))
    else:
        print("Unknown")



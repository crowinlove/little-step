while True:
    sum =0
    a,b = input().split()
    a = a.lower()
    b = b.lower()
    for i  in b:
        if i == a:
            sum +=1
    s = sum/(len(b))
    s1 = "{:.5f}".format(s)
    print(s1)
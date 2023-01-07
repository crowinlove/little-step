while True:
    n = str(input())
    k = 0
    for i in range(len(n)):
        if int(n[i])%2 ==0:
            k = k+int(n[i])
    print(k)
    print()
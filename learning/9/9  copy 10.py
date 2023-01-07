n = int(input())
for i in range(n):
    p,q = input().split()
    t =p.split(".")
    ts = len(t[1])
    pafter = t[1]
    if int(q) <= ts:
        print(pafter[int(q)-1])
    else:
        print(0)
    
n,m = map(int,input().split())
list = []
for i in range(1,n+1):
    list.append(i)
k = m+1
listend = []
while k >=2 :
    k = len(list)
    if k >=m:
        lis1 = list[m-1::m]
        for i in lis1:
            listend.append(i)
        nk = list.index(lis1[-1])
        lisxvt = list[nk+1:]
        lisxvw1 = list[0:nk+1]
        del lisxvw1[m-1::m]
        list = lisxvt+lisxvw1
        k = len(list)
    if k<m and k!=0:
        nk = m
        while nk > k:
            nk -= k
        lisxvt = list[nk:]
        lisxvw1 = list[0:nk-1]
        listend.append(list[nk-1])
        list = lisxvt+lisxvw1
for m in listend:
    print(m,end=" ")



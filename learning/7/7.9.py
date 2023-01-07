lis = input().split()
list = []
t = []
M = int(input())
for i in range(len(lis)):
    n = int(lis[i])
    list.append(n)
for i in range(len(list)):
    n = list[i]
    list2 = list.copy()
    list2.remove(n)
    for j in range(len(list2)):
        q = M - n
        nj = list2[j]
        if q == nj:
            t.append([n,q])
print(t[0][0],t[0][1])
            
        
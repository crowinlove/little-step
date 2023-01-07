n = int(input())
list1 = []
for i in range(n):
    lis = list(map(int,input().split()))
    k = 0
    for j in lis:
        k+=j
    list1.append(k)
list1.sort(reverse=True)
for i in list1:
    print(i,end=" ")
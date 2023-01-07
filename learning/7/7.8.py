N = int(input())
lis = input().split()
list = []
for i in range(N):
    n = int(lis[i])
    list.append(n)
for i in range(N):
    n = int(lis[i])
    k = 0
    for j in range(N):
        m = int(lis[j])
        if m-n>0:
            k =k+1
    print("%d"%k,end=" ")
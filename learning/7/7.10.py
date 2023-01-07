M = int(input())
lis = input().split()
N =int(input())
lis1 = lis.copy()
for i in range(N):
    lis1.insert(0,int(lis1[M-1]))
    lis1.pop()
    print(lis1)
for i in range(M):
    n = int(lis1[i])
    print("%d"%n,end=" ")

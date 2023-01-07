#元组的max()函数只对int起作用>=10,不要用字符串，否则10会比9小，你就噶了
N = int(input())
n = 0
lis = input().split()
list = []
for i in range(N):
    n = int(lis[i])
    list.append(n)
lis1 = list.copy()
lis2 = list.copy()
X,Y = input().split()
X = int(X)
Y = int(Y)
for i in range(X-1):
    m = lis1.count(max(lis1))
    for j in range(m):
        lis1.remove(max(lis1))
maxX = max(lis1)
for i in range(Y-1):
    n = lis2.count(min(lis2))
    for j in range(n):
        lis2.remove(min(lis2))
minY = min(lis2)
print(maxX,minY)
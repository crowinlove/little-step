N = int(input())
lis = input().split()
K = int(input())
i = 1
if N <= 1000 and K<=2100:
    while i <= K+1:
        i = i+1
        list = input().split()
        sum1 = 0
        for i in range(int(list[0])-1,int(list[1])):
            sum1 = sum1+int(lis[i])
        

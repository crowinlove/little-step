import math
def isPrimes(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(math.sqrt(n) + 1), 2):
            if n % x == 0:
                return False
        return True
    return False
m,n =  map(int,input().split())
result = []
sum =0
if 2 <= m<n <= 1000000:
    for i in range(m,n+1):
        lst =  str(i)
        if len(lst)%2 == 0:
            if lst[0:int(len(lst)/2)] == lst[-1:int(len(lst)/2)-1:-1]:
                if isPrimes(i):
                    result.append(i)
        else:
            if lst[0:int((len(lst)-1)/2)] == lst[-1:int((len(lst)-1)/2):-1]:         
                if isPrimes(i): 
                    result.append(i)
for i in result:
    sum += 1
    if sum%10 != 0:
        print(i,end = " ")
    else:
        print(i,end = " ")
        print()
while True:
    def factorial(n):
        factorial  = 1
        for i in range(1,n + 1):
            factorial = factorial*i
        return(factorial)
    n = int(input())
    m = 0
    p = 0
    y1 = 0
    y2 = 0
    if n%2 == 0:
        m = n-1
        p = n
    else:
        m = n
        p = n-1
    for i in range(1,m+1,2):
        y1 += factorial(i)
    for i in range(2,p+1,2):
        y2 += factorial(i)
    print("%d %d"%(y1,y2))


    

n = int(input())
n1 = 0
if 2<= n<=100:
    while n !=1:
        if n%2 == 0:
            n1 = n
            n = int(n/2)
            print(f"{n1}/2={n}")
        else:
            n1 = n
            n = n*3+1
            print(f"{n1}*3+1={n}")
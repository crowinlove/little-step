N = int(input())
for i in range(N):
    n = str(i)
    t = str(i**2)
    if n  in t[len(t)-len(n):len(t)] and i !=0:
        print(i,end=" ")

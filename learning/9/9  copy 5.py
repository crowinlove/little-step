n = int(input())
nstr = str(n)
sum = n
for i in range(n-1):
    nstr = nstr+str(n)
    sum = sum+int(nstr)
print(sum)
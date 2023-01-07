N = input()
n = int(N)
m = 0
c =[]
while n*m <= 2000000000:
    m +=1
    sum = m*n
    sumstr = str(sum)
    b = []
    for  i in sumstr:
        if i == '0' or i == '1':
            b.append(i)
    if len(b)==len(sumstr):
        print(m)
        c.append(m)
        break
if c == []:
    print("No found")
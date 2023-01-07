#判断一个数是不是素数
n = eval(input("n = "))
for i in range(2,n):
    if n % i == 0:
        j = n/i
        print("n = %s * %s" %(i,j))
        break
    elif i == (n-1):
        print("not")

#划重点for else 只有当for正常跑完才会run else那行

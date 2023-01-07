#了解eval
from re import I


x = 1
y  = eval('x+1')
print(y)

#for/while循环
for i  in range(1,11,3):
    print(i)
for letter in 'Python':     # 第一个实例
   print("当前字母: %s" % letter)
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print ('当前水果 : %s' % fruits[index])
foctarial  = 1
n = int(input("input a number: "))
for  i in range(1,n+1):
    foctarial *= i
print(foctarial)


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
      
#进行因式分解
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print("%s 等于 %s * %s" %(num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
sign = -1
s = 0
p = 10
for i in range(1,p+1):
    sign *= -1 
    s += (1/i)*sign
    print(s)


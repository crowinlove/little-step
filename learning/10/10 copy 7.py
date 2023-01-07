#定义阶乘函数
def factrial(n): 
    result = n
    for i in range(1,n):
        result *= i
    if result == 0:
        return 1
    else:
        return result
#定义combine函数（作用是取出所有可能组合）
from itertools import combinations
def combine(temp_list, n):
    temp_list2 = []
    for c in combinations(temp_list, n):
        temp_list2.append(c)
    return temp_list2
#因为题目要求n<=100000，故通过简单计算可知阶乘组成最大应该小于10！而且0！=1
lis = []
for i in range(10):
    lis.append(factrial(i))
'''
lis最终为[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880],
对于题目规定的n已经足够,接下来判断所给的n是不是这些数的组合即可
'''
sumlist  = []
cnm =[]
#sumlist为lis中所有元素的可能组合
for i in range(1,11):
    cnm  = combine(lis, i)
    for j in range(len(cnm)):
        sumi = sum(cnm[j])
        sumlist.append(sumi)
#判断所给数是否在sumlist中
while True:
    p = int(input())
    if p>0 and p in sumlist:
        print('YES')
#考虑特殊情况
    elif p>=0 and p not in sumlist :
        print('NO')
    else:
        break

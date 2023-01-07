'''题目描述【问题】输入N个数,计算数字M的出现次数,并输出M的第一次出现的位置
【输入说明】总共N+2行数据。第一行为数字N。接下来N行,每行一个整数。最后一行为数字M。
在上述的N的数据中查找M第一次出现的位置及总共出现的次数。
【输出要求】输出M首次出现的位置和次数。未找到的位置输出0,次数输出0
【样例输入】
5
52
18
18
654
18
18
【样例输出】
2 3
【说明】n<=100000
'''
N = int(input())
list =[]
for i in range(N):
    n  = int(input())
    list.append(n)
M = int(input())
if M in list:
    nfirstshow = list.index(M) + 1
    m  = list.count(M)
    print(nfirstshow,m)
else:
    print(0,0)
   

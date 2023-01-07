'''
【问题】输入N个数 求它们奇数位之和偶数位之和 并输出它们的差的绝对值

【输入说明】第一行数值n 接下来n行 每行一个整形数字。
【输出要求】第一行输出奇数位和。第二行输出偶数位的和。第三行，将上述大的和减去小的和的差。
【说明】n<=1000
【样例输入】
5
4
6
8
10
12

【样例输出】【解释 不用输出】
24     // {4+8+12}
16     // {6+10}
8      // {24-16}
'''
lisj = []
liso = []
k1 = 0
k2 = 0
N = int(input())
for i in range(N):
    n = int(input())
    if i %2 ==0:
        liso.append(n)
    else:
        lisj.append(n)
for i in range(len(liso)):
    k2 = k2+int(liso[i])
for i in range(len(lisj)):
    k1 = k1+int(lisj[i])
print(k2)
print(k1)
print(abs(k1-k2))
'''
【问题描述】给你一堆杂乱无章的正整数，里面有若干个奇数和偶数（至少有一个奇偶数），
你能编个程序分别找出这堆数中最大的偶数大王和奇数皇后吗？
【输入格式】  第一行N(2<=N<=1000)，第二行接着输入N个正整数a, (a<=100000000)。
【输出格式】 输出所求的偶数大王和奇数皇后
【输入样例】
 5
 12 788 2342281 345 8888888
【输出样例】
 Ou king=8888888
 Ji queen=2342281
'''
N = int(input())
list  = list(map(int,input().split()))
listo = []
listq = []
for i in range(len(list)):
    k = list[i]
    if k%2==0:
        listo.append(k)
    else:
        listq.append(k)
oumax = max(listo)
jimax = max(listq)
print(f'Ou king={oumax}')
print(f'Ji queen={jimax}')

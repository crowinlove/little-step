"""
【问题】输入N*N的矩阵 输出每列的最大值，最小值，每行的最大值，最小值。
【输入说明】第一行整数N。接下来N行为矩阵的数值 每行N个整数。
【输出要求】
第一行N个数值 为每列的最大值。
第二行N个数值 为每列的最小值。
第三行N个数值 为每行的最大值。
第四行N个数值 为每行的最小值。
【说明】n<=1000

【样例输入】：
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
 

【样例输出】：
13 14 15 16
1 2 3 4
4 8 12 16
1 5 9 13
"""
matrix1 = []
matrix = []
N = int(input())
matrixT = []
if N<= 1000:
    for i in range(N):
        s = input().split()
        matrix1.append(s)
    for i in range(N):
        k = []
        for j in range(N):
            k.append(int(matrix1[i][j]))
        matrix.append(k)
    for i in range(N):
        k = []
        for j in range(N):
            k.append(int(matrix[j][i]))
        matrixT.append(k)
    for i in range(N):
        k = max(matrixT[i])
        print(k,end = " ")
    print()
    for i in range(N):   
        k = min(matrixT[i])
        print(k,end = " ")
    print()
    for i in range(N):
        k = max(matrix[i])
        print(k,end = " ")
    print()
    for i in range(N):   
        k = min(matrix[i])
        print(k,end = " ")
    print()
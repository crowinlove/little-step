"""
问题】 输入N*N的矩阵 求矩阵中 P行Q列 Q行P列 的数据。
【输入说明】 第一行整数N。接下来N行 每行N个整数。第N+2行两个整数P和Q。
【输出要求】 两行。第一行为矩阵中P行Q列的数据。第二行为矩阵中Q行P列的数据。

【样例输入】：
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2 4

【样例输出】：
8
14

【说明】n<=3000 内存64M 时间3秒

二维数组 3000*3000 占用内存很大，因此数组变量的定义要放在 int main( )的前面。

读入的数据很多 必须用scanf进行读入 否则给3秒也会超时。
"""
N = int(input())
matrix = []
for i in range(N):
    h  = input().split()
    matrix.append(h)
p,q = (input().split())
P= int(p)
Q= int(q)
print(matrix[P-1][Q-1])
print(matrix[Q-1][P-1])

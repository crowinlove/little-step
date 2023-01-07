
N = int(input())
matrix = []
for i in range(N):
    lst = input().split()
    lst.reverse()
    matrix.append(lst)
matrixT = []
for i in range(N):
    k = []
    for j in range(N):
        k.append(matrix[j][i])
    matrixT.append(k)
for i in range(N):
    for j in range(N):
        print(matrixT[i][j])
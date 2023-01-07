A = input().split()
P = int(A[0])
Q = int(A[1])
matrix = []
for i in range(P):
    h  = input().split()
    matrix.append(h)
matrixT = []
for i in range(Q):
    k = []
    for j in range(P):
        k.append(matrix[j][i])
    matrixT.append(k)

for i in range(Q):
    for j in range(P):
        print(matrixT[i][j],end=" ")
    print()
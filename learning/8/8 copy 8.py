M,N = map(int,input().split())
matrix = []
for i in range(M):
    k = list(map(int,input().split()))
    matrix.append(k)
matrixT = []
I,J = map(int,input().split())

for j in range(N):
    k = []
    for i in range(M):
        k.append(matrix[i][j])
    matrixT.append(k) 
matrixT1 = matrixT.copy()
matrixT[I-1] = matrixT1[J-1]
matrixT[J-1] = matrixT1[I-1]
for i in range(M):
    for j in range(N):
        print(matrixT[j][i],end=" ")
    print()

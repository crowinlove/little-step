matrix = []
j = 0
k = 0
for i in range(6):
    n = list(map(int,input().split()))
    matrix.append(n)
matrix1 = matrix.copy()
for i in range(6):
    j = j+1
    matrix[i][j-1] = 10 + matrix1[i][j-1]
for i in range(6):
    k = k+1
    matrix[i][-k] = 10 + matrix1[i][-k]
for i in range(6):
    for j in range(6):
        print(matrix[i][j],end=" ")
    print()
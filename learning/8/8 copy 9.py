#saddle
from pickle import NONE
from threading import main_thread


m,n = map(int,input().split())
matrix = []
minrow =0 
lst = []
listrow= []
for i in range(m):
    k = list(map(int,input().split()))
    matrix.append(k)
matrixT = []
for j in range(n):
    k = []
    for i in range(m):
        k.append(matrix[i][j])
    matrixT.append(k)
for i in range(m):
    minrow = min(matrix[i])
    for j in range(n):
        if matrix[i][j] == minrow:
            if minrow == max(matrixT[j]):
                lst.append(minrow)
if lst == []:
    print("no find")
else:
    for i in range(m):
        minrow = min(matrix[i])
        for j in range(n):
            if matrix[i][j] == minrow:
                if minrow == max(matrixT[j]):
                    if n<=100 and m<=100:
                        print(i+1,j+1,minrow)
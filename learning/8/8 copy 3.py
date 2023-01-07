N = int(input())
matrix = []
for i in range(N):
    h  = input().split()
    matrix.append(h)
j = 0
sum1 = 0
sum2 = 0
k = 0
if N%2==0:
    for i in range(N):
        j = j+1
        sum1 = sum1 + int(matrix[i][j-1])
    for i in range(N):
        k = k+1
        sum2 = sum2 + int(matrix[i][-k])
else:
    for i in range(N):
        j = j+1
        sum2 = sum2 + int(matrix[i][j-1])
    for i in range(N):
        k = k+1
        sum2 = sum2 + int(matrix[i][-k])
    sum2 = sum2 - int(matrix[int((N+1)/2-1)][int((N+1)/2-1)])
print(sum1+sum2)
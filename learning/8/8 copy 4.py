#两个矩阵的乘积
while True:
    A = []
    B = []
    matrix=[]
    for i in range(2):
        h  = input().split()
        A.append(h)
    for i in range(3):
        h  = input().split()
        B.append(h)
    for i in range(2):
        for j in range(2):
            h = int(A[i][0])*int(B[0][j])+int(A[i][1])*int(B[1][j])+int(A[i][2])*int(B[2][j])
            print(h,end=' ')
        print()

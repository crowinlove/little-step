
m,n = map(int,input().split())
matrix = []
r = 0
for i in range(m):
    k = list(map(int,input().split()))
    matrix.append(k)
print(matrix)
mini= matrix[0][0]
for  i in range(m):
    q = matrix[i]
    p =min(q)
    mini = min(mini,p)
for  i in range(m):
    q = matrix[i]
    p =min(q) 
    if p == mini:
        print(mini,i+1,int(q.index(mini))+1)
        break



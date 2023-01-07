N = int(input())
k = list(map(int,input().split()))
k1 = set(k)
listn = []
list = []
for i in k1:
    counti = k.count(i)
    list.append([counti,i])
    listn.append(counti)
maxi = max(listn)
list.sort(key= lambda x : x[1])
for  i in list:
    if i[0] == maxi:
        print(i[1],i[0])

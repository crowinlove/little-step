n=int(input())
yuansu=['H','C','N','O','F','P','S','K']
fenziliang=[1,12,14,16,19,31,32,39]
a=dict(zip(yuansu,fenziliang))
b=[]
for i in range(n):
    op = input()
    fenzishi=[i for i in op ]
    count=0
    for j in range(len(fenzishi)):
        if str.isalpha(fenzishi[j]):
            count+=a[fenzishi[j]]
        else:
            count+=(int(fenzishi[j])-1)*a[fenzishi[j-1]]
    print(count)
N = int(input())
list1 = []
list2 = []
for i in range(N):
    i = input()
    list1.append(i)
    j = i.split()
    k = float(j[4])
    list2.append(k)
dic =  dict(zip(list2,list1))
ranlist = sorted(list2,reverse=True)
for i  in range(len(list2)):
    print(dic[ranlist[i]])
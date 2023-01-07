
a,b = input().split()
a = list(a)
b = list(b)
a1 = a.copy()
a1[int(len(a)/2)-1:int(len(a)/2)]=b
a1.insert(int(len(a)/2)-1,a[int(len(a)/2)-1])
print(a1)
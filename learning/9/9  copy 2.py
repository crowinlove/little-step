m,b = map(int,input().split())
lst = list(map(int,input().split()))
lst1 = [i for i in lst if (i+b)%b != 0 ]
lst1.sort()
for i in range(len(lst1)):
    if 65 <= lst1[i] <= 90:
        print(chr(lst1[i]).upper(),end = " ")
    else:
        print(lst1[i],end=" ")
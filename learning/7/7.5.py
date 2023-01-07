'''  在读入的包括n个整数的数组中查找
是否有元素等于读入的Ｘ,如果没有找到则输出“no”
如果找到则在数组中将这个数删除,然后输出删除该元素后的新数组。 
(如果数组中有多个元素等于X,查找并删除第一个等于X的元素。)

包括三行 第一行有一个整数n 第二行有n个整数 第三行有一个整数X 为要查找的数。

如果没有找到则输出“no” 如果找到则在数组中将这个数删除 然后输出删除该元素后的新数组。
'''
N = int(input())
lis = input().split()
list= []
X = int(input())
for i in range(N):
    n = int(lis[i])
    list.append(n)
if X in list:
    list.remove(X)
    for i in range(len(list)):
        n = int(list[i]) 
        print(n,end=" " )
else:
    print("no")
    
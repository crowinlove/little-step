#输入十个自然数，将第一个转移到最后一个
from typing import List


lis = input().split()
list = lis.copy()
list.pop(0)
list.append(lis[0])
for i in range(10):
    n = int(list[i]) 
    print("%4d"%n,end="" )
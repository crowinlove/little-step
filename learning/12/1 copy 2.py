'''
明明想在学校中请一些同学一起做一项问卷调查，
为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数(N≤100)，
对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。
'''
num_count = int(input())
inputnum = map(int,input().split())
outnumber = set(inputnum)
list1 = sorted(list(outnumber))
print(len(list1))
for i in range(len(list1)):
    print(list1[i],end=" ")


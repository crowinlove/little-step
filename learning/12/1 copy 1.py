'''
A是B的一个真子集，输出“A is a proper subset of B”；
B是A的一个真子集，输出“B is a proper subset of A”；
A和B是同一个集合，输出"A equals B”；
A和B的交集为空，输出"A and B are disjoint”；
上述情况都不是，输出“I'm confused!”。
'''
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C =set()
A1 = A[1:]
B1 = B[1:]
A2 = set(A1)
B2 = set(B1)
if A2 == B2:
    print("A equals B")
elif A2 > B2:
    print("B is a proper subset of A")
elif B2 > A2:
    print("A is a proper subset of B")
elif A2&B2 == C:
    print("A and B are disjoint")
else:
    print("I'm confused!")
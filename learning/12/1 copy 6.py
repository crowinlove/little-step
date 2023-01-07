'''
0～59、60～69、70～79、80～89和90～100各分数段的人数
'''
n = int(input())
n_059 = 0
n_6069 = 0
n_7079 = 0
n_8089 = 0
n_90100 = 0
for i  in range(n):
    i = int(input())
    if i in range(0,60):
        n_059+=1
    if i in range(60,70):
        n_6069+=1
    if i in range(70,80):
        n_7079+=1
    if i in range(80,90):
        n_8089+=1
    if i in range(90,101):
        n_90100+=1
print(n_059)
print(n_6069)
print(n_7079)
print(n_8089)
print(n_90100)
#汉罗塔
n  = int(input())
def ban(n,x1,x2,x3):
    if n ==1 :
        print(f'{x1}->{x3}')
        return
    else:
        ban(n-1,x1,x3,x2)
        print(f'{x1}->{x3}')
        ban(n-1,x2,x1,x3)
ban(n,"A","B","C")


n = int(input())
if n % 2 == 0 and n % 3 == 0 and n % 5 == 0: 
    print("能被2整除 能被3整除 能被5整除") 
elif n % 2 == 0 and n % 3 == 0:
    print("能被2整除 能被3整除")
elif n % 3 == 0 and n % 5 == 0:
    print("能被3整除 能被5整除")
elif n % 2 == 0 and n % 5 == 0:
    print("能被2整除 能被5整除")
elif n % 2 == 0:
    print("能被3整除")   
elif n % 3 == 0:
    print("能被3整除")
elif n % 5 == 0:
    print("能被5整除")
    
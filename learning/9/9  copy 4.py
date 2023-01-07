lst = str(input())
alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in lst:
    if i.isalpha():
        index = alphalist.index(i)
        lst = lst.replace(i,alphalist[index+4])
print(lst)
n=int(input())



for i in range(n):
    for j in range(n):
        if n-i-1<=j :
            print('*',end='')

    print()




for i in range(n):
    for j in range(n):
        if i>=j :
           pass
        else :
            print("*",end='')
    print()

n=int(input())

for i in range(n):
    for j in range(2*n):
        if i%2==0 and j%2==0 :
            print("*",end='')
        elif i%2!=0 and j%2!=0 :
            print("*",end='')
        else :
            print(" ",end='')
    print()
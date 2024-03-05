n=int(input())

for i in range(n):
    for j in range(2*n-1):
        if i+n-1>=j and j>=n-i-1 :
            print('*',end='')
        elif  j<=n-i-1:
            print(" ",end='')
    print()
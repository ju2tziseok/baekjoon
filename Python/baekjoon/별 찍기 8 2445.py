n=int(input())

for i in range(n) :
    for j in range(2*n) :
        if i>=j or 2*n-i-1<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in range(n-1):
    for j in range(2*n):
        if n-i-2>=j or 2*n-(n-1)+i<=j:
            print('*',end='')
        else:
            print(" ",end='')
    print()

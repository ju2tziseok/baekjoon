t=int(input())
for i in range(t):
    n=int(input())
    b=(bin(n)[2:])[::-1]

    for j in range(len(b)):
        if b[j]=='1':
            print(j,end=' ')
    print()

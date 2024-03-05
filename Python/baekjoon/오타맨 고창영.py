n=int(input())
li=[]
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=list(b)
    del b[a-1]

    for j in b :
        print(j,end='')
    print()


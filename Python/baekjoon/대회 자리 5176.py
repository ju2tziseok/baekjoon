t=int(input())

for i in range(t):
    p,m=map(int,input().split())
    se = set()
    for j in range(p):

        a=int(input())
        se.add(a)

    print(p-len(se))
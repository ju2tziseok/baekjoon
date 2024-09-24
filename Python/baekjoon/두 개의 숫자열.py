def calculate(n,m,data1,data2) :
    k=[]
    if n>m :
        for i in range(0,n-m+1) :
            s=0
            for j in range(m) :
                s+=data1[i+j]*data2[j]
            k.append(s)
    elif n<m :
        for i in range(0,m-n+1):
            s=0
            for j in range(n):
                s+=data1[j]*data2[i+j]
            k.append(s)
    return max(k)
t=int(input())

for i in range(1,t+1) :
    n,m=map(int,input().split())
    data1=list(map(int,input().split()))
    data2=list(map(int,input().split()))
    print(f"#{i} {calculate(n,m,data1,data2)}")
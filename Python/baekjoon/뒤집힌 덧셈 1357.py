a,b=map(int,input().split())

def rev(n):
    res=0
    while n>0 :
        a=n%10
        res=res*10+a
        n=n//10
    return res

print(rev(rev(a)+rev(b)))


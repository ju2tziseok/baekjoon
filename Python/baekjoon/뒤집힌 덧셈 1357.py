a,b=map(int,input().split())

def rev(n):
    res=str(n)[::-1]
    res=int(res)
    return res

print(rev(rev(a)+rev(b)))


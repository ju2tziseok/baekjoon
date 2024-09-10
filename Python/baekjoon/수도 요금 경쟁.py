def water(p,q,r,s,w) :
    a=p*w

    if r>=w :
        b=q
    else :
        b=q+s*(w-r)

    return min(a,b)




t=int(input())

for i in range(t) :
    P,Q,R,S,W=map(int,input().split())
    print(f"#{i+1} {water(P,Q,R,S,W)}")
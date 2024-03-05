t=int(input())

for i in range(t):
    a,b=input().split()
    cnt=[]
    for j in range(len(a)) :
       if ord(a[j])<=ord(b[j]) :
           cnt.append(ord(b[j])-ord(a[j]))
       else:
           cnt.append(ord(b[j])+26-ord(a[j]))

    print(f"Distances: {' '.join(map(str,cnt))}")
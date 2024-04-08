n=int(input())
dic={}

for i in range(n) :
    a,b=input().split()
    if b=="enter":
       dic[a]=True
    elif b=="leave":
        del dic[a]

print("\n".join(sorted(dic.keys(),reverse=True)))
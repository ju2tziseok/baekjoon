w=[]
k=[]
for i in range(20):
    if i<=9 :
        w.append(int(input()))
    else :
        k.append(int(input()))




w.sort(reverse=True)
k.sort(reverse=True)
print(sum(w[:3]),sum(k[:3]))
li=[0]*26
s=input()

for i in range(len(s)) :
    li[ord(s[i])-97]+=1


for i in li :
    print(i,end=' ')

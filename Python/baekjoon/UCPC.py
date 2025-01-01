s=input()

d=["U","C","P","C"]
cnt=0
j=0
for i in range(len(s)) :
    if j==4 :
        break
    if s[i] == d[j] :
        cnt+=1
        j+=1


if cnt==4 :
    print("I love UCPC")
else :
    print("I hate UCPC")
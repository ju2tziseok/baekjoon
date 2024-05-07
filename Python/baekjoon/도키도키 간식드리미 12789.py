n=int(input())
line=list(map(int,input().split()))
stack=[]
s=1
cnt=0
while cnt<n :
    if s==line[cnt] :
        s+=1
        cnt+=1
    else :
        if len(stack) >0 and s ==stack[-1] :
            stack.pop()
            s+=1
        else :
            stack.append(line[cnt])
            cnt+=1


if len(stack)==0 :
    print("Nice")
else :
    while len(stack) >0 and s ==stack[-1] :

        stack.pop()
        s+=1
    if len(stack)==0 :
        print("Nice")
    else :
        print("Sad")






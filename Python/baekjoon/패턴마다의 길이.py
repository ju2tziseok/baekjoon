t=int(input())

for i in range(1,t+1) :
    text=input()
    tmp=[]

    for j in range(1,11) :
        if text[:j]==text[j:2*j]:
            print("#%d %d"%(i,j))
            break
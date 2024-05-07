import sys
n,m=map(int,sys.stdin.readline().split())
dic={}
for i in range(n):
    s=sys.stdin.readline().rstrip()

    if len(s)>=m :
        if s in dic :

            dic[s]+=1
        else :
            dic[s]=0
dic=dict(sorted(dic.items(),key=lambda item:(-dic[item[0]], -len(item[0]), item[0])))

for i in dic :
    print(i)
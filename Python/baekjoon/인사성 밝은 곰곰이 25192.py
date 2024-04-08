def check(n):
    li=set()
    cnt=0
    for i in range(n):
        s=input()
        if  s!='ENTER' :
            if s not in li:
                cnt+=1
                li.add(s)

        elif s=='ENTER':
            li.clear()

print(check(int(input())))








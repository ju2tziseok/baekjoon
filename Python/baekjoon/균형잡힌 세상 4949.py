


while True:
    s=input()
    li=[]
    if s=='.' :
        break

    for i in s :
        if i=='(' or i=='[' :
            li.append(i)
        elif i==')':
            if len(li)!=0 and li[-1]=='(':
                li.pop()
            else :
                li.append(i)
        elif i==']':
            if len(li) != 0 and li[-1] == '[':
                li.pop()
            else:
                li.append(i)

    if len(li)==0 :
        print("yes")
    else :
        print("no")
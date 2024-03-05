s=input()
li=[]
for i in s :
    if ord(i)>=65 and ord(i)<=77 :
        li.append(chr(ord(i)+13))
    elif ord(i)>77 and ord(i)<=90 :
        li.append(chr(ord(i)-13))
    elif ord(i)>=97 and ord(i)<=109 :
        li.append(chr(ord(i)+13))
    elif ord(i)>109 and ord(i)<=122 :
        li.append(chr(ord(i)-13))
    else :
        li.append(i)

for i in li :
    print(i,end='')



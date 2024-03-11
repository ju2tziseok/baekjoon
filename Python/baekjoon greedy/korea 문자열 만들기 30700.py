cnt=0
kor=['K','O','R','E','A']
j=0
s=input()

for i in s:
    if i==kor[j]:
        j+=1
        cnt+=1
    if j==5 :
        j=0

print(cnt)




t=int(input())

for i in range(t):
    a=input()
    if a[0].isupper() :
        print(a)
    else :
        a=a[0].upper()+a[1:]
        print(a)
n=int(input())
s=input()

if s.count("S")+1+s.count("LL")>n:
    print(n)
else :
    print(s.count("S")+1+s.count("LL"))

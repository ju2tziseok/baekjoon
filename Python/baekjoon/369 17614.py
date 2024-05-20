import sys
n=int(sys.stdin.readline())
b=0
for i in range(1,n+1) :
    d= str(i).count("3")+str(i).count("6")+str(i).count("9")
    b+=d
print(b)
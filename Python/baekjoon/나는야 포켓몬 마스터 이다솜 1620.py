import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

dic_number={}
dic_name={}

for i in range(n):
    a=sys.stdin.readline().rstrip()
    dic_number[i]=a
    dic_name[a]=i

for i in range(m):
    s=sys.stdin.readline().rstrip()
    if s.isdigit():
        print(dic_number[int(s)-1])
    else:
        print(dic_name[s]+1)


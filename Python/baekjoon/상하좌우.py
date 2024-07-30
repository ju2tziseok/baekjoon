n=int(input())

start_x=1
start_y=1

data=list(input().split())

for i in data :
    if i=='L'and start_y>1:
        start_y-=1
    elif i=="R" and start_y<n:
        start_y+=1
    elif i=="U" and start_x >1:
        start_x-=1
    elif i=="D" and start_x <n:
        start_x+=1
print(start_x,start_y)
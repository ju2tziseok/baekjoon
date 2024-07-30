data=input()

x=int(data[1])
y=int(ord(data[0]))-96


steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
cnt=0
for step in steps :
    next_x=x+step[0]
    next_y=y+step[1]

    if next_x>=1 and next_y>=1 and next_x<=8 and next_y<=8 :
        cnt+=1

print(cnt)
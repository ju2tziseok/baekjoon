n=int(input())

for i in range(n):
    li=list(map(int,input().split()))
    temp=li[1:]
    temp.sort()
    cnt = []
    for j in range(li[0]-1):
        cnt.append(abs(temp[j]-temp[j+1]))

    print(f"Class {i+1}")
    print(f"Max {max(temp)}, Min {min(temp)}, Largest gap {max(cnt)}")
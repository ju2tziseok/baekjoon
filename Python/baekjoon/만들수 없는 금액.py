n=int(input())
data=list(map(int,input().split()))

data.sort()
target=1

for i in data :
    if i>target :
        break
    else :
        target+=1
print(target)
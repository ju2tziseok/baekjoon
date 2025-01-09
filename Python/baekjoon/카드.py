n=int(input())

data=dict()

for i in range(n) :
    a=int(input())
    if a in data :
        data[a]+=1
    else :
        data[a]=1

max_data=max(data.values())
min_index=float("inf")
for key, value in data.items() :
    if value == max_data :
        min_index=min(min_index,key)

print(min_index)
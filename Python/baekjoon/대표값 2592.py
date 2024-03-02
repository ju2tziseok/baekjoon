cnt=[0]*1001
sum=0
for i in range(10):
    a=int(input())
    sum+=a
    cnt[a]+=1

print(sum//10)
print(cnt.index(max(cnt)))

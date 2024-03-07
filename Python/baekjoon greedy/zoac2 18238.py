s=input()
time=0
start='A'
for i in s:
    left=ord(start)-ord(i)
    right=ord(i)-ord(start)

    if left <0 :
        left+=26
    elif right<0:
        right+=26

    time+=min(left,right)
    start=i

print(time)
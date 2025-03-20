n=int(input())
house=list(map(int,input().split()))
house.sort()
median=house[(n-1)//2]
print(median)

import heapq

heap=[]

n=int(input())

for i in range(n):
    heapq.heappush(heap,int(input()))


if n == 1 :
    print(0)
elif n == 2 :
    print(heap[0]+heap[1])
else :
    res = 0
    while len(heap) > 1 :
        first =heapq.heappop(heap)
        second =heapq.heappop(heap)
        cnt = first + second
        res+=cnt
        heapq.heappush(heap,cnt)

    print(res)
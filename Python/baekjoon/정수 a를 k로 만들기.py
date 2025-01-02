from collections import deque

a,k=map(int,input().split())

visited=[False]*(k+1)

def bfs(a) :
    cnt = 0
    queue=deque()
    queue.append([a,cnt])

    while queue :

        a,cnt=queue.popleft()
        visited[a]=True
        if a==k :
            print(cnt)
            return

        if a+1 <= k and not visited[a+1] :
            queue.append((a+1,cnt+1))
        if a*2 <= k and not visited[a*2] :
            queue.append((a*2,cnt+1))


bfs(a)
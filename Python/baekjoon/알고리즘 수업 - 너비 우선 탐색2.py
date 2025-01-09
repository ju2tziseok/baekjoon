from collections import deque
import sys
input = sys.stdin.readline

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
cnt=1

for _ in range(m) :
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph :
    g.sort(reverse=True)

def bfs(graph,v,visited) :
    global cnt
    queue=deque()
    queue.append(v)
    visited[v]=cnt

    while queue :
        v=queue.popleft()

        for i in graph[v] :
            if visited[i] == 0 :
                cnt+=1
                queue.append(i)
                visited[i]=cnt

bfs(graph,v,visited)

for i in range(1,n+1) :
    print(visited[i])
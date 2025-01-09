import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0] *(n+1)

cnt=1

def dfs(graph,v,visited) :
    global cnt
    visited[v]=cnt

    for i in graph[v] :
        if visited[i] == 0 :
            cnt+=1
            dfs(graph,i,visited)

for i in range(m) :
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph :
    g.sort()

dfs(graph,v,visited)

for i in range(1,n+1):
    print(visited[i])
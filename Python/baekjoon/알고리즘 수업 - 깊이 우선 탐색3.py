import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
depth=[-1]*(n+1)

for _ in range(m) :
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph :
    g.sort()

def dfs(v,current_depth) :
    depth[v] = current_depth

    for i in graph[v] :
        if depth[i] == -1 :
            dfs(i,current_depth+1)

dfs(v,0)

for i in range(1,n+1) :
    print(depth[i])
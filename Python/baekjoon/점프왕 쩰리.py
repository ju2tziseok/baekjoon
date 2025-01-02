n=int(input())

graph=[]

for i in range(n) :
    graph.append(list(map(int,input().split())))

def dfs(x,y,visited) :
    if x<0 or y<0 or x>=n or y>=n :
        return False
    if visited[x][y] :
        return False
    if graph[x][y]==-1 :
        return True

    visited[x][y]=True

    jump=graph[x][y]
    if dfs(x+jump,y,visited) or dfs(x,y+jump,visited) :
        return True
    return False



visited=[[False]*n for _ in range(n)]


if dfs(0,0,visited) :
    print("HaruHaru")
else :
    print("Hing")
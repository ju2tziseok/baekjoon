graph=[]

for i in range(5):
    graph.append(list(map(int,input().split())))

x,y=map(int,input().split())

bool=False

def dfs(x,y,cnt,move):
    global bool
    if x<0 or x>4 or y<0 or y>4 or move >3 :
        return
    if graph[x][y]==-1 :
        return
    if graph[x][y]==1 :
        cnt+=1

    temp=graph[x][y]
    graph[x][y]=-1

    if cnt==2 :
        bool=True
        return

    dfs(x+1,y,cnt,move+1)
    dfs(x-1, y, cnt, move + 1)
    dfs(x, y+1, cnt, move + 1)
    dfs(x, y-1, cnt, move + 1)
    graph[x][y]=temp

dfs(x,y,0,0)

if bool :
    print(1)
else:
    print(0)
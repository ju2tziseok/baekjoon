from itertools import combinations

n,m=map(int,input().split()) # n x n 크기 m 치킨집 최대 개수
array=[]

for _ in range(n) :
    array.append(list(map(int,input().split())))

chickens=[]
houses=[]

for i in range(n) :
    for j in range(n) :
        if array[i][j] == 1 :
            houses.append((i+1,j+1))
        elif array[i][j] == 2 :
            chickens.append((i+1,j+1))

candidates = list(combinations(chickens,m))

def get_sum(candidate) :
    result = 0
    for hx,hy in houses :
        temp = 1e9
        for cx,cy in candidate :
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
        result+=temp
    return result



result = 1e9
for candidate in candidates :
    result = min(result,get_sum(candidate))

print(result)





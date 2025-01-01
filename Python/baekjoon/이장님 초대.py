n=int(input())
tree=list(map(int,input().split()))

tree.sort(reverse=True)
day=1

for i in range(len(tree)):

    tree[i]+=(-n+1)+i

print(n+1+max(tree))
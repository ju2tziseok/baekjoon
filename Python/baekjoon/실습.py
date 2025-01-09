n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))


for i in range(k):
    a_min_index = a.index(min(a))
    b_max_index = b.index(max(b))
    a[a_min_index], b[b_max_index] = b[b_max_index], a[a_min_index]

print(sum(a))

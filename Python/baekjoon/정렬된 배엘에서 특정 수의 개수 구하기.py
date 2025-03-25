from bisect import bisect_left ,bisect_right

def count_by_range(array,left_index,right_index) :
    right_index = bisect_right(array,right_index)
    left_index = bisect_left(array,left_index)
    return right_index - left_index


n,x=map(int,input().split())
#n은 원소 개수
#x는 찾고자 하는 수
array=list(map(int,input().split()))



cnt = count_by_range(array,x,x)

if cnt == 0 :
    print(-1)
else :
    print(cnt)

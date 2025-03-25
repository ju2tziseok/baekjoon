def binary_search(array) :
    start = 0
    end = len(array)-1
    while start <= end :
        mid = (start+end)//2
        if array[mid] == mid :
            return mid
        elif array[mid] > mid :
            end = mid -1
        elif array[mid] < mid :
            start = mid + 1

    return None


n=int(input())
array=list(map(int,input().split()))

result = binary_search(array)

if result == None :
    print(-1)
else :
    print(result)
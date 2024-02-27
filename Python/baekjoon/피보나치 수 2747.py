memo = {}
def f(n):

    if n in memo :
        return memo[n]
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        temp=f(n-1)+f(n-2)
        memo[n]=temp
        return temp

n=int(input())
print(f(n))
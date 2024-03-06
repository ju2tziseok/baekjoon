import sys
case=[0]*91
def fibonacci(case,n):
    if n==0 :
        case[n]=0
        return case[n]
    elif n==1 :
        case[n]=1
        return case[n]
    else:
        case[n]=fibonacci(n-1)+fibonacci(n-2)
        return case[n]


n=int(sys.stdin.readline())
print(fibonacci(case,n))
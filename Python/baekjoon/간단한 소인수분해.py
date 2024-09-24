#소인수분해 함수 설계 : 리스트에 저장
#오직 2 3 5 7 11로만 구성됨

def prime_factors(n) :
    factors=[2,3,5,7,11]
    cnt=[0]*5
    i = 0
    while n>1 and i<len(factors):

        if n%factors[i]==0 :
            cnt[i]+=1
            n//=factors[i]
        else :
            i+=1


    return cnt



t=int(input())

for i in range(t):
    n=int(input())
    print(f"#{i+1}",end=' ')
    for j in prime_factors(n) :
        print(j,end=' ')
    print()

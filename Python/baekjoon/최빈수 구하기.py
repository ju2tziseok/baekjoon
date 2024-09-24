def count(data) :
    grade=[0]*101

    for i in range(1000) :

        grade[data[i]]+=1

    max_frequency = max(grade)

    mode=0
    for i in range(101) :
        if grade[i]==max_frequency :
            mode=i

    return mode



t=int(input())

for i in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    print(f"#{n} {count(data)}")


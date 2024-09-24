def rc(n) :
    distance=0
    speed=0
    for i in range(n) :
        command=list(map(int,input().split()))

        if command[0]==1 :
            speed+=command[1]
        elif command[0]==2 :
            speed-=command[1]
            if speed < 0:
                speed = 0

        distance+=speed
    return distance

t=int(input())

for i in range(1,t+1):
    n=int(input())
    result=rc(n)
    print(f"#{i} {result}")

n=int(input())

game=[str(x) for x in range(1,n+1)]



for i in range(n) :
    cnt = game[i].count("3")+game[i].count("6")+game[i].count("9")

    if cnt == 1 :
        game[i]="-"
    elif cnt==2 :
        game[i]="--"
    elif cnt==3 :
        game[i]="---"

for i in game :
    print(i,end=' ')







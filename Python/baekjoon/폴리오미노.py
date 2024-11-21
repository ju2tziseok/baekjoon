board=input()
a=board.count(".")

if (len(board)-a)%2!=0 :
    print(-1)

else :
    board_parts=board.split(".")
    res=""
    for parts in board_parts :

        if parts :
            cnt = len(parts)
            while cnt>0 :
                if cnt >= 4 :
                    cnt-=4
                    res+="AAAA"
                elif cnt>=2 :
                    cnt-=2
                    res+="BB"
                else :
                    print(-1)
                    exit()
        res+="."

    print(res[:len(res)-1])
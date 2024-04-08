n = int(input())
for i in range(n):
    stack = []
    s=input()

    for i in s:

        if i == "(":
             stack.append(i)
        elif i == ")":

            if len(stack)==0:
                stack.append(")")
                break
            else :
                stack.pop()

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")








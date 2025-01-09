n=int(input())
book=dict()

for i in range(n):
    x=input()
    if x in book :
        book[x]+=1
    else :
        book[x]=1

array=dict(sorted(book.items(),key=lambda item : (-book[item[0]],item[0])))

array=list(array.keys())
print(array[0])
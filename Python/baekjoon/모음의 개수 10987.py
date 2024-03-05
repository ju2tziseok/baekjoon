vowel=['a','e','i','o','u']
a=input()
res=0
for i in range(5):
    res+=a.count(vowel[i])

print(res)
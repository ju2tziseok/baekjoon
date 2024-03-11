# 리스트 내포(list comprehension)
# 반복가능한 것을 기반으로
# 새로운 리스트를 만들어내는 문법

#An=2n+1(0<=n<10)
#A={1,3,5,7,9,...,19}

A=[]

for i in range(0,10):
    A.append(2*i+1)
print(A)

[표현식 for 반복문]
A=[2*i+1 for i in range(0,10)]

A=[
    2*i+1 #표현식
    for i in range(0,10)#반복문
    if i%2==0 #조건문
]
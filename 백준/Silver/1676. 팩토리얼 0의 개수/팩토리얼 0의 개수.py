from math import factorial
N=int(input())
num=str(factorial(N))
for i in range(len(num)-1,-1,-1):
    if num[i]!='0':
        print(len(num)-(i+1))
        break

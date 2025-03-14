from math import factorial
for tc in range(int(input())):
    n=int(input())
    a=str(factorial(n))
    for i in range(len(a)-1,-1,-1):
        if a[i]!='0':
            print(a[i])
            break
import math
count=0
N=int(input())
for y in range(N):
    if (N+1+y)%3==0:
        count+= (math.factorial(N-1))//((math.factorial(N-1-y))*(math.factorial(y)))
print(count%1000000007)
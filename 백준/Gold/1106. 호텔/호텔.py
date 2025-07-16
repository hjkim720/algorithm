import sys
input = sys.stdin.readline
C,N=map(int,input().split())
lst=list(list(map(int,input().split())) for _ in range(N))
dp=[10000000]*100000
dp[0]=0
for cost, client in lst:
    for i in range(client, 100000):
        if dp[i]>dp[i-client]+cost:
            dp[i]=dp[i-client]+cost
print(min(dp[C:]))

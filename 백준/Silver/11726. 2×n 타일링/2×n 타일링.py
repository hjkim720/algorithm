N=int(input())
dp=[0]*(N+1)
dp[1]=1
if N>1:
    dp[2]=2
    if N>2:
        dp[3]=3
for i in range(4,N+1):
    dp[i]=dp[i-2]+dp[i-1]
print(dp[N]%10007)
N,T=map(int,input().split())
lst=list(list(map(int,input().split())) for _ in range(N))
dp=[0]*(T+1)
for w,v in lst:
    for i in range(T,w-1,-1):
        dp[i]=max(dp[i],dp[i-w]+v)
print(dp[T])
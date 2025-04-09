N,M = map(int,input().split())
activated=list(map(int,input().split()))
deactivated=list(map(int,input().split()))
M=sum(activated)-M
lst=list(zip(activated,deactivated))
dp=[0]*(M+1)
for w,v in lst:
    for i in range(M,w-1,-1):
        dp[i]=max(dp[i],dp[i-w]+v)
print(sum(deactivated)-dp[M])
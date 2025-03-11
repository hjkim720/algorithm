N=int(input())
wine=[]
for _ in range(N):
    wine.append(int(input()))
dp=[0]*(N)
dp[0]=wine[0]
if N>1:
    dp[1]=wine[0]+wine[1]
for i in range(2,N):
    dp[i]=max(dp[i-1],dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i])
print(dp[-1])
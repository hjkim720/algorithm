N=int(input())
lst=list(map(int,input().split()))
# dp를 만들어요
dp=[0]*N
for i in range(N):
    # dp[i]는 lst[i] (자기자신)과 dp[i-1](그전까지의 최댓값(누적 또는 아님))+lst[i](자기자신) 중 큰 값을 저장
    dp[i]=max(lst[i],dp[i-1]+lst[i])
print(max(dp))
N= int(input())
stamina=list(map(int,input().split()))
happiness=list(map(int,input().split()))
lst=list(zip(stamina,happiness))
dp=[0]*100
for w,v in lst:
    for i in range(99,w-1,-1):
        dp[i]=max(dp[i],dp[i-w]+v)
print(dp[99])
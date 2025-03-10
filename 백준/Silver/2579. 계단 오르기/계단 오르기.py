N=int(input())
lst=[int(input()) for _ in range(N)]
dp=[0]*N
if len(lst)<=2:
    print(sum(lst))
else:
    dp[0]=lst[0]
    dp[1]=lst[0]+lst[1]
    for i in range(2,N):
        dp[i]=max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])
    print(dp[-1])
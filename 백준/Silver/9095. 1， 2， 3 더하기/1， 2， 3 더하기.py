T=int(input())
for tc in range(T):
    N=int(input())
    # dp를 만들어요
    dp=[0]*(N+1)
    dp[1]=1
    if N>1:
        dp[2]=2
        if N>2:
            dp[3]=4
        for i in range(4,N+1):
            dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    print(dp[N])
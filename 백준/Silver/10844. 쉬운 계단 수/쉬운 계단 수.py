N=int(input())
dp=[[0]*10 for _ in range(N+1)]
for num in range(1,10):
    dp[1][num]=1
for row in range(2,N+1):
    for col in range(10):
        if col==0:
            dp[row][col]=dp[row-1][1]%1000000000
        elif col==9:
            dp[row][col]=dp[row-1][8]%1000000000
        else:
            dp[row][col]=dp[row-1][col-1]+dp[row-1][col+1]%1000000000
print(sum(dp[N])%1000000000)
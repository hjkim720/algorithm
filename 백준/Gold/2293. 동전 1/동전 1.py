import sys
input=sys.stdin.readline
N,K=map(int,input().split())
coins=list(int(input()) for _ in range(N))
dp=[0]*(K+1)
# 초깃값 설정 때문에 꽤나 고민함.
# dp[0]을 1로 두면 dp[coin]이 자동적으로 1이 됨
# 그러나 드는 의문은 for coin in coins: dp[coin]=1로 짜면 왜 안되냐는 것
dp[0]=1
for coin in coins:
    for i in range(coin,K + 1):
        dp[i]+=dp[i-coin]
print(dp[K])
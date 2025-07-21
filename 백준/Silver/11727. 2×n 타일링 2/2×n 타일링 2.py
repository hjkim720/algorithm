n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    #10007을 곱해서 틀렸다. 실수 주의하자
    dp[i] = (dp[i-1]%10007 + 2*dp[i-2]%10007) % 10007
print(dp[n])

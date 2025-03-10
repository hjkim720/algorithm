N=int(input())
dp=[1]*10
#0으로 끝나는 애-> 항상 1개(0)
#n자리수에서 1의자리 k가 나오는 경우의 수->n-1자리수에서 0부터 k-1까지 sum
for i in range(N-1):
    for j in range(1,10):
        dp[j]+=dp[j-1]
print(sum(dp)%10007)



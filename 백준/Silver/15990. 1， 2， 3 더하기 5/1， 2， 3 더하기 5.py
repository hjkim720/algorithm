'''
<내 뇌 속>
1로 끝내려면 직전보고
2로 끝내려면 두 개 전 보고
3으로 끝내려면 세 개 전 보면 되겠네
'''
dp=[[0]*3 for _ in range(100001)]
dp[1][0]=1
dp[2][1]=1
dp[3][0],dp[3][1],dp[3][2]=1,1,1
for i in range(4,100001):
        # i 번째에서
        # 1로 끝나는 경우는 i-1번째 1로 끝나는 경우의 수 + i-1번째 2로 끝나는 경우의 수
        dp[i][0]=(dp[i-1][1]+dp[i-1][2])%1000000009
        # 2로 끝나는 경우는 i-2번째 전 1로 끝나는 경우의 수 + i-2번째 3으로 끝나는 경우의 수
        dp[i][1]=(dp[i-2][0]+dp[i-2][2])%1000000009
        # 3으로 끝나는 경우는 i-3번째 전 1로 끝나는 경우의 수 + i-3번째 전 2로 끝나는 경우의 수
        dp[i][2]=(dp[i-3][0]+dp[i-3][1])%1000000009
T=int(input())
for tc in range(T):
    N=int(input())
    print(sum(dp[N])%1000000009)
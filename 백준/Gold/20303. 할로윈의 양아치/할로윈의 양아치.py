def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x=find(x)
    ref_y=find(y)
    if ref_x==ref_y:
        return
    elif ref_x>ref_y:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x

N,M,K=map(int,input().split())
candies=list(map(int,input().split()))
parent=list(range(len(candies)+1))

for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)
res=[]
for items in set(parent[1:]):
    tmp=0
    cnt=0
    for i in range(1,len(parent)):
        if find(i)==items:
            tmp+=candies[i-1]
            cnt+=1
    res.append((cnt,tmp))


def knapsack(tuples):
    # DP 테이블 초기화
    dp = [0] * (K+1)  # K 미만이므로 dp 크기를 K로 설정 (0 ~ K-1)

    # 모든 튜플을 하나씩 고려하며 DP 갱신
    for weight, value in tuples:
        # 무게 제한을 초과하지 않는 범위에서 역순으로 업데이트
        for w in range(K - 1, weight - 1, -1):  # K 미만이어야 하므로 K-1까지
            dp[w] = max(dp[w], dp[w - weight] + value)

    return max(dp)  # 가능한 값 중 최댓값 반환
print(knapsack(res))
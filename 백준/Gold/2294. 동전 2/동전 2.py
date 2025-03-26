# 문제를 보자마자 BFS가 떠올랐음(추후 DP로 다시 풀어볼 예정)
# 왜 BFS가 떠올랐냐? ->최소 갯수 = 최단경로
# 시작 위치를 0으로 두고 타겟인 K로 출발
# 한번에 coins 리스트(입력받은 coin의 종류)에 있는 coin칸을 갈 수 있다고 해석할 수 있음
from collections import deque
import sys
input=sys.stdin.readline
def bfs():
    q=deque()
    q.append(0)
    visited=[K+1]*(K+1)
    visited[0]=0
    while q:
        t=q.popleft()
        if t==K:
            return visited[t]
        for coin in coins:
            w=t+coin
            if w<=K and visited[w]>visited[t]+1:
                visited[w]=visited[t]+1
                q.append(w)
    return -1

N,K=map(int,input().split())
coins=[int(input()) for _ in range(N)]
print(bfs())
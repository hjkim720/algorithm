import heapq
import sys
input=sys.stdin.readline
N=int(input())
q=[]
for i in range(N):
    n=int(input())
    if n:
        heapq.heappush(q,-n)
    else:
        tmp=0
        if q:
            tmp=heapq.heappop(q)
        # 이상한 실수를 계속한다..자야겠다
        print(-tmp)

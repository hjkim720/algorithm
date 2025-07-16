import heapq
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
bosuks=list(list(map(int,input().split())) for _ in range(N))
bags=list(int(input()) for _ in range(K))
bosuks.sort(reverse=True)
# bags를 reverse=True 넣고 sort한게 원흉이었다.
bags.sort()
q=[]
res=0
for bag in bags:
    while bosuks:
        weight, cost=bosuks.pop()
        if bag>=weight:
            heapq.heappush(q,-cost)
        else:
            bosuks.append((weight,cost))
            break
    if q:
        res-=heapq.heappop(q)
print(res)


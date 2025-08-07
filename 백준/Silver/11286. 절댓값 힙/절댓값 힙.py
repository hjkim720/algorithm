import heapq
import sys
input = sys.stdin.readline
N=int(input())
lst=[]
for _ in range(N):
    i=int(input())
    if i:
        heapq.heappush(lst,(abs(i),i))
        continue
    else:
        if lst:
            o=heapq.heappop(lst)
            print(o[1])
        else:
            print(0)
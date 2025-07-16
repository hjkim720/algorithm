import sys
import heapq

input = sys.stdin.readline
q = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(q, num)
    else:
        print(heapq.heappop(q) if q else 0)

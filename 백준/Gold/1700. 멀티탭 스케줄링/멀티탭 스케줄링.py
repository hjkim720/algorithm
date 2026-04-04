from collections import deque
import sys
input=sys.stdin.readline
N, K = map(int,input().split())
lst=deque(map(int,input().split()))
occupied=set()
cnt=0
for i in range(K):
    tmp=lst.popleft()
    if tmp in occupied: continue
    if len(occupied)<N:
        occupied.add(tmp)
        continue
    who=0
    far=-1
    for item in occupied:
        if item not in lst:
            who=item
            break
        tmp_far=lst.index(item)
        if tmp_far>far:
            far=tmp_far
            who=item
    occupied.remove(who)
    occupied.add(tmp)
    cnt+=1
print(cnt)
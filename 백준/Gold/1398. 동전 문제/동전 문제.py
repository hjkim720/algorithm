from collections import deque
import sys
input=sys.stdin.readline
dir=(25,10,1)
def bfs(num):
    q=deque()
    q.append(0)
    visited=[0]*(num+1)
    visited[0]=1
    while q:
        t=q.popleft()
        if t==num:
            return visited[num]
        for d in dir:
            w=t+d
            if w<=num and not visited[w]:
                q.append(w)
                visited[w]=visited[t]+1
                
T=int(input())
for tc in range(T):
    N=int(input())
    res=0
    while N>0:
        tmp=N%100
        res+=bfs(tmp)-1
        N=N//100
    print(res)
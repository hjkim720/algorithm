from collections import deque
def bfs():
    q=deque()
    q.append(N)
    visited=[float('inf')]*100001
    visited[N]=0
    while q:
        t=q.popleft()
        if 2*t<=100000 and visited[2*t]>visited[t]:
            visited[2*t]=visited[t]
            q.append(2*t)
        if t==K:
            return visited[t]
        for choices in (t+1,t-1):
            if 0<=choices<=100000 and visited[choices]>visited[t]+1:
                visited[choices]=visited[t]+1
                q.append(choices)
N,K = map(int,input().split())
print(bfs())
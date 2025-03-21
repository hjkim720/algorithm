from collections import deque
def bfs():
    q=deque()
    q.append(N)
    visited=[100001]*100001
    visited[N]=0
    flag=False
    while q:
        t=q.popleft()

        if not flag and t == K:
            flag=True
            res=visited[t]
            cnt=1
        elif flag and t==K:
            cnt+=1

        for choices in (t + 1, t - 1,2*t):
            if 0 <= choices <= 100000 and visited[choices] >= visited[t] + 1:
                visited[choices] = visited[t] + 1
                q.append(choices)
    return (res,cnt)

N,K=map(int,input().split())
print(*bfs(),sep='\n')

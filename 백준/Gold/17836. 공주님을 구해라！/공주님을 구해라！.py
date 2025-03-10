from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def find_sword():
    for i in range(N):
        for j in range(M):
            if castle[i][j]==2:
                return [i,j]
def bfs(ei,ej):
    q=deque()
    q.append((0,0))
    visited=[[0]*M for _ in range(N)]
    visited[0][0]=1
    while q:
        ti,tj=q.popleft()
        if (ti,tj) == (ei,ej):
            return visited[ti][tj],(ti,tj)
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and  not visited[wi][wj] and castle[wi][wj]!=1:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1
    return float('inf'),(0,0)
    

N,M,T=map(int,input().split())
castle=[list(map(int,input().split())) for _ in range(N)]
si,sj=find_sword()
to_sword,cur_loc=bfs(si,sj)
sword_dist=to_sword-1+abs(N-1-cur_loc[0])+abs(M-1-cur_loc[1])
dist,tmp=bfs(N-1,M-1)
res=min(sword_dist,dist-1)
if res<=T:
    print(res)
else:
    print('Fail')
import sys
input=sys.stdin.readline
from collections import deque
q=deque()
def find_ripe():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if lst[i][j][k]==1:
                    q.append((i,j,k))
    return q

def bfs(q):
    dir = ((1,0,0),(0,0,1),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1))
    visited=[list([0]*M for _ in range(N)) for _ in range(H)]
    for tomato in q:
        visited[tomato[0]][tomato[1]][tomato[2]]=1
    while q:
        ti, tj, tk = q.popleft()
        for d in dir:
            wi,wj,wk=ti+d[0],tj+d[1],tk+d[2]
            if 0<=wi<H and 0<=wj<N and 0<=wk<M and lst[wi][wj][wk]==0 and not visited[wi][wj][wk]:
                q.append((wi,wj,wk))
                visited[wi][wj][wk]=visited[ti][tj][tk]+1
                lst[wi][wj][wk]=1
    days=visited[0][0][0]
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k]>days:
                    days=visited[i][j][k]
                if lst[i][j][k]==0:
                    return -1
    return days-1

M,N,H = map(int,input().split())
lst=[]
for h in range(H):
    tmp=list(list(map(int,input().split())) for _ in range(N))
    lst.append(tmp)
print(bfs(find_ripe()))
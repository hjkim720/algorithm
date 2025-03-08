from collections import deque
tunnel_type={1:((1,0),(0,1),(-1,0),(0,-1)),
             2:((1,0),(-1,0)),
             3:((0,1),(0,-1)),
             4:((-1,0),(0,1)),
             5:((1,0),(0,1)),
             6:((1,0),(0,-1)),
             7:((-1,0),(0,-1))}

def bfs(si,sj):
    global cnt
    q=deque()
    q.append((si,sj))
    visited=[[0]*M for _ in range(N)]
    visited[si][sj]=1
    while q:
        ti,tj=q.popleft()
        if visited[ti][tj]>L:
            return 
        for d in tunnel_type[grid[ti][tj]]:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and grid[wi][wj]!=0 and visited[wi][wj]==0:
                for d in tunnel_type[grid[wi][wj]]:
                    zi,zj=wi+d[0],wj+d[1]
                    if zi==ti and zj==tj:
                        q.append((wi,wj))
                        visited[wi][wj]=visited[ti][tj]+1
                        if L>=visited[wi][wj]>=1 and (wi,wj) not in counted:
                            counted.append((wi,wj))
T=int(input())
for testcase in range(1,T+1):
    counted=deque()
    N,M,R,C,L=map(int,input().split())
    grid=[list(map(int,input().split())) for _ in range(N)]
    bfs(R,C)
    print(f'#{testcase} {len(counted)+1}')
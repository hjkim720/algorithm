from collections import deque
dir=((1,0),(0,1),(-1,0),(0,-1))
def bfs(si,sj):
    global cnt
    q=deque()
    q.append((si,sj))
    visited=[[0]*M for _ in range(N)]
    visited[si][sj]=1
    farm[si][sj]=cnt
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and farm[wi][wj]=='cabbage' and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=1
                farm[wi][wj]=cnt
    cnt+=1

T=int(input())
for testcase in range(T):
    M,N,K=map(int,input().split())
    farm=[['empty']*M for _ in range(N)]
    cnt=1
    coordinates=[]
    for _ in range(K):
        j,i=map(int,input().split())
        farm[i][j]='cabbage'
        coordinates.append((i,j))
    for coor in coordinates:
        if farm[coor[0]][coor[1]]=='cabbage':
            bfs(coor[0],coor[1])
    print(cnt-1)

    
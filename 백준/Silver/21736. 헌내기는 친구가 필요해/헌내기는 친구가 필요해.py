from collections import deque
N,M=map(int,input().split())
campus=[list(map(str,input())) for _ in range(N)]
is_found=False
for i in range(N):
    for j in range(M):
        if campus[i][j]=='I':
            doyeon=(i,j)
            is_found=True
            break
    if is_found:
        break
cnt=0    
q=deque()
q.append(doyeon)
visited=[[0]*M for _ in range(N)]
visited[doyeon[0]][doyeon[1]]==1
dir=((1,0),(-1,0),(0,1),(0,-1))
while q:
    ti,tj=q.popleft()
    if campus[ti][tj]=='P':
        cnt+=1
    for d in dir:
        wi,wj=ti+d[0],tj+d[1]
        if 0<=wi<N and 0<=wj<M and campus[wi][wj]!='X' and visited[wi][wj]==0:
            q.append((wi,wj))
            visited[wi][wj]=1
print(cnt if cnt else 'TT')
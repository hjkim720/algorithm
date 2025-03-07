from collections import deque
dir=((1,0),(-1,0),(0,1),(0,-1))
def bfs(si,sj):
    global group_num
    cnt=1
    q=deque()
    q.append((si,sj))
    visited=[[0]*N for _ in range(N)]
    visited[si][sj]=1
    apt[si][sj]=group_num
    while q:
        ti,tj=q.popleft()
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<N and apt[wi][wj]==1 and visited[wi][wj]==0:
                q.append((wi,wj))
                visited[wi][wj]=visited[ti][tj]+1
                apt[wi][wj]=group_num
                cnt+=1
    group_num+=1
    return cnt

N=int(input())
apt=[list(map(int,input())) for _ in range(N)]
#아파트 아파트 아파트 아파트 아파트 아파트 어 어어어어~
group_num=2
res=[]
for i in range(N):
    for j in range(N):
        if apt[i][j]==1:
            res.append(bfs(i,j))

print(group_num-2)
res.sort()
for items in res:
    print(items)

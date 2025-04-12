from collections import deque
dir_dic={1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
def bfs():
    q=deque()
    q.append((si,sj,sd))
    visited=[[[0]*5 for _ in range(N)]for _ in range(M)]
    visited[si][sj][sd]=1
    while q:
        ti,tj,td=q.popleft()
        if (ti,tj,td)==(ei,ej,ed):
            return visited[ti][tj][td]-1
        for idx in dir_dic:
            if idx==td:
                for k in range(1,4):
                    wi,wj,wd=ti+k*dir_dic[idx][0],tj+k*dir_dic[idx][1],idx
                    if 0<=wi<M and 0<=wj<N and not grid[wi][wj]:
                        if not visited[wi][wj][wd]:
                            visited[wi][wj][wd]=visited[ti][tj][td]+1
                            q.append((wi,wj,wd))
                    else:
                        break
            else:
                if not visited[ti][tj][idx]:
                    if (td,idx) not in ((1,2),(2,1),(3,4),(4,3)):
                        visited[ti][tj][idx]=visited[ti][tj][td]+1
                        q.append((ti,tj,idx))              
M,N = map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(M))
si,sj,sd=map(int,input().split())
si,sj=si-1,sj-1
ei,ej,ed=map(int,input().split()) 
ei,ej=ei-1,ej-1
print(bfs())
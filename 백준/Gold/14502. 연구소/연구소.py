from copy import deepcopy
from itertools import combinations

def virus(t):
    q=[]
    cnt=0
    for i in range(N):
        for j in range(M):
            if t[i][j]==2:
                q.append([i,j])
            
            
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    visited=[[0]*M for _ in range(N)]
    for start_loc in q:
        visited[start_loc[0]][start_loc[1]]=1
    while q:
        ti,tj=q.pop(0)
        for d in dir:
            wi,wj=ti+d[0],tj+d[1]
            if 0<=wi<N and 0<=wj<M and t[wi][wj]!=1 and visited[wi][wj]==0:
                q.append([wi,wj])
                visited[wi][wj]=1
                t[wi][wj]=2
    for i in range(N):
        for j in range(M):
            if t[i][j]==0:
                cnt+=1
    return cnt
N,M=map(int,input().split())
lab=[list(map(int,input().split())) for _ in range(N)]
z=[]
result=[]
for i in range(N):
        for j in range(M):
            if lab[i][j]==0:
                z.append([i,j])
choices=list(combinations(z,3))
for i in choices:
    temp_lab=deepcopy(lab) 
    for j in range(3):
        temp_lab[i[j][0]][i[j][1]]=1  
    result.append(virus(temp_lab))
print(max(result))

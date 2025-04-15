import sys
sys.setrecursionlimit(2000)
def dfs(now,total,visited):
    global res
    if total>=res:
        return
    if all(visited) and grid[now][0]:
        res=min(res,total+grid[now][0])
        return
    for i in range(N):
        if not visited[i] and grid[now][i]:
            visited[i]=1
            dfs(i,total+grid[now][i],visited)
            visited[i]=0


N=int(input())
grid=list(list(map(int,input().split())) for _ in range(N))
v=[0]*N
v[0]=1
res=21e9
dfs(0,0,v)
print(res)

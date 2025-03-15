import sys
input=sys.stdin.readline
def dfs(si,sj,status):
    global cnt
    if (si,sj)==(N-1,N-1):
        cnt+=1
        return 
    if status==0:
        if sj+1<N and grid[si][sj+1]!=1: dfs(si,sj+1,0)
        if si+1<N and sj+1<N and grid[si+1][sj+1]!=1 and grid[si+1][sj]!=1 and grid[si][sj+1]!=1:dfs(si+1,sj+1,2)
    elif status==1:
        if si+1<N and grid[si+1][sj]!=1: dfs(si+1,sj,1)
        if si+1<N and sj+1<N and grid[si+1][sj+1]!=1 and grid[si+1][sj]!=1 and grid[si][sj+1]!=1:dfs(si+1,sj+1,2)
    
    else:
        if si+1<N and grid[si+1][sj]!=1:dfs(si+1,sj,1)
        if sj+1<N and grid[si][sj+1]!=1:dfs(si,sj+1,0)
        if si+1<N and sj+1<N and grid[si+1][sj+1]!=1 and grid[si+1][sj]!=1 and grid[si][sj+1]!=1:dfs(si+1,sj+1,2)
N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
cnt=0
dfs(0,1,0)
print(cnt)
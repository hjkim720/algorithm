def dfs(si,sj,word):
    if len(word)== 6:
        res.add(word)
        return
    if si+1<5:
        dfs(si+1,sj,word+str(grid[si+1][sj]))
    if si-1>=0:
        dfs(si-1,sj,word+str(grid[si-1][sj]))
    if sj+1<5:
        dfs(si,sj+1,word+str(grid[si][sj+1]))
    if sj-1>=0:
        dfs(si,sj-1,word+str(grid[si][sj-1]))
    else:
        return

grid=[list(map(int,input().split())) for _ in range(5)]
res=set()
for i in range(5):
    for j in range(5):
        dfs(i,j,str(grid[i][j]))
print(len(res))
def dfs(si,sj,word):
    if len(word)== 7:
        res.add(word)
        return
    if si+1<4:
        dfs(si+1,sj,word+str(grid[si+1][sj]))
    if si-1>=0:
        dfs(si-1,sj,word+str(grid[si-1][sj]))
    if sj+1<4:
        dfs(si,sj+1,word+str(grid[si][sj+1]))
    if sj-1>=0:
        dfs(si,sj-1,word+str(grid[si][sj-1]))
    else:
        return
T=int(input())
for testcase in range(1,T+1):
    grid=[list(map(int,input().split())) for _ in range(4)]
    res=set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(grid[i][j]))
    print(f'#{testcase} {len(res)}')

def dfs(i,cnt):
    global visited,res
    # 갱신
    res = max(res,cnt)
    for nodes in graph[i]:
        if not visited[nodes]:
            visited[nodes]=1
            dfs(nodes,cnt+1)
            visited[nodes]=0
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    res=0
    for i in range(1,N+1):
        visited = [0] * (N + 1)
        if not visited[i]:
            visited[i]=1
            dfs(i,1)
    print(f'#{tc} {res}')
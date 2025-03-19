def dfs(i):
    global visited
    for nodes in graph[i]:
        if not visited[nodes]:
            visited[nodes]=1
            dfs(nodes)
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited=[0]*(N+1)
    cnt=0
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            cnt+=1
    print(f'#{tc} {cnt}')
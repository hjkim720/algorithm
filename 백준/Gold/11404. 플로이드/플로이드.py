import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
graph=[[21e9]*N for _ in range(N)]
for _ in range(M):
    a,b,w=map(int,input().split())
    graph[a-1][b-1]=min(graph[a-1][b-1],w)


for i in range(N):
    for j in range(N):
        if i==j:
            graph[i][j]=0
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
for i in range(N):
    for j in range(N):
        print(graph[i][j] if graph[i][j]<21e9 else 0,end=' ')
    print()

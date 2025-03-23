import sys
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x=find(x)
    ref_y=find(y)
    if ref_x==ref_y:
        return
    elif ref_y>ref_x:
        parent[ref_y]=ref_x
    else:
        parent[ref_x]=ref_y
V,E=map(int,input().split())
parent=list(range(V+1))
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    if find(u)!=find(v):
        union(u,v)
for i in range(1,V):
    if find(i)!=find(i+1):
        print('NO')
        break
else:
    cnt=0
    for i in range(1,V+1):
        if len(graph[i])%2==1:
            cnt+=1
    if cnt==0 or cnt==2:
        print('YES')
    else:
        print('NO')

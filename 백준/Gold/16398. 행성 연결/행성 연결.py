import sys
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x,y=find(x),find(y)
    if x==y:
        return
    if x>y:
        parent[x]=y
    else:
        parent[y]=x
N=int(input())
parent=list(range(N))
costs=list(list(map(int,input().split())) for _ in range(N))
graph=[]
for i in range(N):
    for j in range(i+1,N):
        graph.append((i,j,costs[i][j]))
graph.sort(key=lambda x:x[2])
cnt=0
res=0
for s,e,w in graph:
    if find(s)!=find(e):
        union(s,e)
        res+=w
        cnt+=1
        if cnt==N-1:
            break
print(res)
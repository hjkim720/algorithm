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
    elif ref_x<ref_y:
        parent[ref_y]=ref_x
    else:
        parent[ref_x]=ref_y
N=int(input())
parent=list(range(N+1))
for _ in range(N-2):
    u,v=map(int,input().split())
    if find(u)!=find(v):
        union(u,v)
print(*set(find(x) for x in range(1, N+1)))

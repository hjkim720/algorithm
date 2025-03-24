import sys
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x,ref_y=find(x),find(y)
    if ref_x==ref_y:
        return
    elif ref_x>ref_y:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x
N,M=map(int,input().split())
parent=list(range(N+1))
for _ in range(M):
    u,v=map(int,input().split())
    if find(u)!=find(v):
        union(u,v)
print(len(set(find(x) for x in range(1, N+1))))
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
parent=list(range(V))
graph=[[] for _ in range(V)]
res=0
for i in range(1,E+1):
    u,v=map(int,input().split())
    if res!=0:
        continue
    if find(u)==find(v):
        res=i
    union(u,v)
print(res)
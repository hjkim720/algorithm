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
        size[ref_y]+=size[ref_x]
    else:
        parent[ref_y]=ref_x
        size[ref_x]+=size[ref_y]
T=int(input())
for tc in range(T):
    parent={}
    F=int(input())
    size= {}
    for _ in range(F):
        u,v=input().split()
        if u not in parent:
            parent[u]=u
            size[u]=1
        if v not in parent:
            parent[v]=v
            size[v]=1
        union(u,v)
        print(size[find(u)])
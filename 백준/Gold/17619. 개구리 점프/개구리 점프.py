import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x,ref_y=find(x),find(y)
    if ref_x==ref_y:
        return
    if ref_x>ref_y:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x
N,Q=map(int,input().split())
parent=list(range(N+1))
coord=[]
for i in range(1,N+1):
    x1,x2,y=map(int,input().split())
    coord.append((x1,x2,i))
coord.sort()
for index in range(1,N):
    if coord[index-1][0]<=coord[index][0]<=coord[index-1][1] and find(coord[index][2])!=find(coord[index-1][2]):
        union(coord[index][2],coord[index-1][2])
for _ in range(Q):
    s,e=map(int,input().split())
    if find(s)==find(e):
        print(1)
    else:
        print(0)

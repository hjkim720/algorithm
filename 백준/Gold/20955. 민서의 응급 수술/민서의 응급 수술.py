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
N,M=map(int,input().split())
parent=list(range(N+1))
cnt=0
for _ in range(M):
    u,v=map(int,input().split())
    if find(u)==find(v):
        cnt+=1
    union(u,v)
components = len(set(find(x) for x in range(1, N+1)))
print(cnt + components - 1)

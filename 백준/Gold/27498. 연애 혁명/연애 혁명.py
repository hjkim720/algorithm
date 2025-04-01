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
    if ref_x>ref_y:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x
N,M=map(int,input().split())
parent=list(range(N+1))
graph=[]
standard=N-1
for _ in range(M):
    a,b,c,d=map(int,input().split())
    if d==1:
        union(a,b)
        standard-=1
    else:
        graph.append((a,b,c))
res=0
cnt=0
graph.sort(key=lambda x:x[2],reverse=True)
for s,e,w in graph:
    if find(s)==find(e):
        res += w
    else:
        union(s,e)
print(res)
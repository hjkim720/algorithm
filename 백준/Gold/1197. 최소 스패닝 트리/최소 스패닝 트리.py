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
    if ref_y>ref_x:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x
N,M=map(int,input().split())
parent=list(range(N+1))
cnt=0
lst=[]
res=0
lst=list(list(map(int,input().split())) for _ in range(M))
lst.sort(key=lambda x:x[2])
for s,e,w in lst:
    if find(s)!=find(e):
        union(s,e)
        cnt+=1
        res+=w
        if cnt==N-1:
            print(res)
            break
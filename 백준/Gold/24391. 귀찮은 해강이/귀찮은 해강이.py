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
    if ref_x>ref_y:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x

N,M=map(int,input().split())
parent=list(range(N+1))
for _ in range(M):
    i,j = map(int,input().split())
    union(i,j)
lst=list(map(int,input().split()))
cnt=0
for i in range(len(lst)-1):
    if find(lst[i])!=find(lst[i+1]):
        cnt+=1
print(cnt)
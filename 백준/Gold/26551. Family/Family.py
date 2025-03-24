def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x=find(x)
    ref_y=find(y)
    if ref_x==ref_y:
        return
    if temp=='mom' or 'dad' or 'brother' or 'sister':
        parent[ref_y]=ref_x
    else:
        parent[ref_x]=ref_y
N=int(input())
parent={}
lst=[]
for _ in range(N):
    u,temp,v=input().split()
    parent[u]=u
    parent[v]=v
    lst.append((u,temp,v))
for items in lst:
    if find(items[0])!=find(items[2]):
        temp=items[1]
        union(items[0],items[2])
M=int(input())
for _ in range(M):
    a,b=input().split()
    if find(a)==find(b):
        print('Related')
    else:
        print('Not Related')

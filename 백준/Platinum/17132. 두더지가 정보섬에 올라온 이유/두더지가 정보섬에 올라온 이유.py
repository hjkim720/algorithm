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
    
    else:
        if size[ref_x]>size[ref_y]:
            ref_x,ref_y=ref_y,ref_x
        size[ref_y]+=size[ref_x]
        parent[ref_x]=ref_y
N=int(input())
parent=list(range(N+1))
info=[]
for _ in range(N-1):
    temp=list(map(int,input().split()))
    info.append(temp)
info.sort(key=lambda x:x[2], reverse=True)
res=0
size=[1]*(N+1)
for u,v,weight in info:
    ru,rv=find(u),find(v)
    if ru!=rv:
        res+=weight*size[ru]*size[rv]
        union(u,v)
print(res)
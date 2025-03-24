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
N=int(input())
parent=list(range(10**6+1))
size=[1]*(10**6+1)
for _ in range(N):
    action,*lst=input().split()
    if action == 'I':
        a,b=map(int,lst)
        union(a,b)
    else:
        print(size[find(int(*lst))])
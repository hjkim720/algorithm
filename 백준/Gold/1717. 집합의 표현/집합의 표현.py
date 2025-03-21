def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x=find(x)
    ref_y=find(y)
    if ref_x==ref_y:
        return
    elif ref_x>ref_y:
        parent[ref_y]=ref_x
    else:
        parent[ref_x]=ref_y
n,m = map(int,input().split())
parent=list(range(n+1))
for _ in range(m):
    operation, a, b = map(int,input().split())
    if operation == 0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
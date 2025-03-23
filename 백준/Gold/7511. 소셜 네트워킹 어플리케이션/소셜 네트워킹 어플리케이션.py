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
T=int(input())
for testcase in range(1,T+1):
    
    N=int(input())
    K=int(input())
    parent=list(range(N+1))
    for _ in range(K):
        a,b=map(int,input().split())
        union(a,b)
    M=int(input())
    print(f'Scenario {testcase}:')
    for _ in range(M):
        u,v=map(int,input().split())
        if find(u)==find(v):
            print(1)
        else:
            print(0)
    print()

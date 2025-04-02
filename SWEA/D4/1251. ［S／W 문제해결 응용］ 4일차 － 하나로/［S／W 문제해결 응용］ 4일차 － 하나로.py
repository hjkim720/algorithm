def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    x,y=find(x),find(y)
    if x==y:
        return
    if x>y:
        parent[x]=y
    else:
        parent[y]=x
T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    parent=list(range(N))
    x_coord=list(map(int,input().split()))
    y_coord=list(map(int,input().split()))
    coords=list(zip(x_coord,y_coord))
    graph=[]
    E=float(input())
    for i in range(N-1):
        for j in range(i+1,N):
            graph.append((i,j,((coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2)*E))
    graph.sort(key=lambda x:x[2])
    cnt=0
    res=0
    for s,e,w in graph:
        if find(s)!=find(e):
            union(s,e)
            res+=w
            cnt+=1
            if cnt==N-1:
                break
    print(f'#{testcase} {round(res)}')

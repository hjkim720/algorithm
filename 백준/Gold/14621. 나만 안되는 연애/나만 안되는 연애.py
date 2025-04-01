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
boy_girl=list(input().split())
lst=list(list(map(int,input().split())) for _ in range(M))
lst.sort(key=lambda x:x[2])
res=0
cnt=0
for s,e,w in lst:
    if boy_girl[s-1]!=boy_girl[e-1] and find(s)!=find(e):
        union(s,e)
        res+=w
        cnt+=1
        if cnt==N-1:
            print(res)
            break
else:
    print(-1)
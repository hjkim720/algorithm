N,M=map(int,input().split())
lst=list(map(int,input().split()))
res=[]
lst.sort()
visited=[0]*(max(lst)+1)
def perm(cnt):
    if cnt==M:
        print(*res)
        return
    for items in lst:
        if not visited[items]:
            visited[items]=1
            res.append(items)
            perm(cnt+1)
            res.pop()
            visited[items]=0
perm(0)
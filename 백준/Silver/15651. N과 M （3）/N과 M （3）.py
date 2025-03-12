N,M=map(int,input().split())
res=[]
def perm(cnt):
    if cnt==M:
        print(*res)
        return
    for i in range(1,N+1):
        res.append(i)
        perm(cnt+1)
        res.pop()
perm(0)
N,M=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
res=[]
def perm_with_rep(cnt):
    if cnt==M:
        print(*res)
        return
    for items in lst:
        if res:
            if items>=res[-1]:
                res.append(items)
                perm_with_rep(cnt+1)
                res.pop()
        else:
            res.append(items)
            perm_with_rep(cnt + 1)
            res.pop()
perm_with_rep(0)
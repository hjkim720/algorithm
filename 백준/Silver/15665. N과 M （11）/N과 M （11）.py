N,M=map(int,input().split())
lst=list(map(int,input().split()))
res=[]
lst.sort()
lst=set(lst)
def perm(cnt):
    if cnt==M:
        print(*res)
        return
    for items in lst:
        res.append(items)
        perm(cnt+1)
        res.pop()

perm(0)
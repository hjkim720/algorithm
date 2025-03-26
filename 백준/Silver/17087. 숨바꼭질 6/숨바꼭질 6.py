N,S=map(int,input().split())
Aoos=list(map(int,input().split()))
dists=list(abs(Aoo-S) for Aoo in Aoos)
res=min(dists)
for dist in dists:
    p,q=dist,res
    while p%q!=0:
        r=p%q
        p=q
        q=r
    res=q
print(res)
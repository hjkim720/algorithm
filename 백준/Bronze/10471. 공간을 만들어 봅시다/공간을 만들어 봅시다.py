w,p=map(int,input().split())
lst=list(map(int,input().split()))
res=set()
res.add(w)
for i in range(p):
    res.add(lst[i])
    res.add(w-lst[i])
    for j in range(i+1,p):
        res.add(lst[j]-lst[i])
res=sorted(list(res))
print(*res)

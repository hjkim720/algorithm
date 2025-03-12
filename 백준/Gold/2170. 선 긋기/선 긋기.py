N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
lst.sort()
res=0
cur=float('-inf')
for items in lst:
    s,e=items[0],items[1]
    if cur<=s:
        res+=e-s
    elif s<cur<e:
        res+=e-cur

    if cur<=e:
        cur=e
print(res)
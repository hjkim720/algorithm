import sys
input=sys.stdin.readline
N,S=map(int,input().split())
lst=list(map(int,input().split()))
e=0
tmp=0
res=21e9
for s in range(N):
    while e<N and tmp<S:
        tmp+=lst[e]
        e+=1
    if tmp>=S:
        res=min(res,e-s)
    tmp-=lst[s]
print(res if res<21e9 else 0)

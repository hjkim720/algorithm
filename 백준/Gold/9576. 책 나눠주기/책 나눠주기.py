T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    wish=[list(map(int,input().split())) for _ in range(M)]
    wish.sort(key=lambda x:x[1])
    taken=[0]*(N+1)
    res=0
    for a,b in wish:
        for book in range(a,b+1):
            if not taken[book]:
                taken[book]=1
                res+=1
                break
    print(res)
T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    lst=[]
    for _ in range(N):
        lst.append(list(map(int,input().split())))
    corridor=[0]*201
    for routes in lst:
        s,e=routes[0],routes[1]
        if s>e:
            s,e=e,s
        s=(s-1)//2
        e=(e-1)//2
        for i in range(s,e+1):
            corridor[i]+=1
    print(f'#{testcase} {max(corridor)}')

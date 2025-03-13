from itertools import combinations
T= int(input())

for testcase in range(1,T+1):
    res = float('inf')
    N,B=map(int,input().split())
    lst=list(map(int,input().split()))
    for i in range(1,N+1):
        for items in combinations(lst,i):
            tmp=sum(items)
            if B<=tmp<res:
                res=tmp
    print(f'#{testcase} {res-B}')
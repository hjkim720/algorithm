T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    local_max=0
    profit=0
    for i in range(N-1,-1,-1):
        if lst[i]>local_max:
            local_max=lst[i]
        else:
            profit+=local_max-lst[i]
    print(f'#{testcase} {profit}')
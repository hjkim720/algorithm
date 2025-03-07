T=int(input())
for testcase in range(1,T+1):
    N=int(input())
    cnt=0
    lst=[list(map(int,input().split())) for _ in range(N)]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if (lst[i][0]>lst[j][0] and lst[i][1]>lst[j][1]) or (lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]):
                continue
            cnt+=1
    print(f'#{testcase} {cnt}')
def dfs(cnt,visited):
    global res
    if cnt==switch:
        res=max(res,int(''.join(lst)))
        return
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            lst[i],lst[j]=lst[j],lst[i]
            n=int(''.join(lst))
            if (n,cnt) not in visited:
                visited.append((n,cnt))
                dfs(cnt+1,visited)
            lst[i],lst[j]=lst[j],lst[i]
T=int(input())
for testcase in range(1,T+1):
    tmp,switch=map(int,input().split())
    lst=[digit for digit in str(tmp)]
    res=0
    dfs(0,[])
    print(f'#{testcase} {res}')
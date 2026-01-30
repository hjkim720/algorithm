N=int(input())
lst=list(map(int,input().split()))
lst.sort()
res=0
for j in range(N+1):
    res+=sum(lst[0:j])
print(res)
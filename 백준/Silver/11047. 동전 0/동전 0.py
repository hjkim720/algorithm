N,K=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(int(input()))

cnt=0
lst.sort(reverse=True)
i=0
while K:
    if K//lst[i]==0:
        i+=1
    else:
        cnt+=K//lst[i]
        K=K%lst[i]
print(cnt)
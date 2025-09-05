import sys
input=sys.stdin.readline
N,K,P=map(int,input().split())
lst=list(map(int,input().split()))
i=0
res=0
while i<=(N-1)*K:
    cnt=0
    for j in range(K):
        if lst[i+j]==0:
            cnt+=1
    if cnt>=P:
        res+=1
    i+=K
print(N-res)
N,M=map(int,input().split())
lst=list(map(int,input().split()))
total=0
for i in range(N-1,-1,-1):
    total+=lst[i]
    if total>=M:
        print(i+1)
        break
else:
    print(-1)
import sys
input=sys.stdin.readline
N=int(input())
lst=list(map(int,input().split()))
lst.sort()
cnt=0
for i in range(N):
    s=0
    e=N-1
    while s<e:
        if lst[s]+lst[e]==lst[i]:
            if s==i:
                s+=1
            elif e==i:
                e-=1
            else:
                cnt+=1
                break
        elif lst[s]+lst[e]>lst[i]:
            e-=1
        elif lst[s]+lst[e]<lst[i]:
            s+=1
print(cnt)


import sys
N=int(input())
lst=list(map(int,input().split()))
lst.sort()
tmp=21e9
for i in range(N-2):
    j=i+1
    k=N-1
    while j<k:
        if abs(lst[i]+lst[j]+lst[k])<tmp:
            tmp=abs(lst[i]+lst[j]+lst[k])
            res=[lst[i],lst[j],lst[k]]
        if tmp==0:
            break
        
        if lst[i]+lst[j]+lst[k]>0:
            k-=1
        elif lst[i]+lst[j]+lst[k]<0:
            j+=1
        
print(*sorted(res))
        
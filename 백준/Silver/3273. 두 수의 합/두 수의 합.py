import sys
input=sys.stdin.readline
N=int(input())
lst=list(map(int,input().split()))
lst.sort()
t=int(input())
s,e=0,N-1
cnt=0
while s<e:
    if lst[s]+lst[e]==t:
        cnt+=1
        s+=1
    elif lst[s]+lst[e]<t:
        s+=1
    else:
        e-=1
print(cnt)
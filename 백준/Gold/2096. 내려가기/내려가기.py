import sys
input=sys.stdin.readline
N=int(input())
tmp=list(map(int,input().split()))
ma=tmp
mi=tmp
for i in range(N-1):
    lst=list(map(int,input().split()))
    ma=[lst[0]+max(ma[0],ma[1]),lst[1]+max(ma[1],ma[2],ma[0]),lst[2]+max(ma[1],ma[2])]
    mi = [lst[0] + min(mi[0], mi[1]), lst[1] + min(mi[1], mi[2], mi[0]), lst[2] + min(mi[1], mi[2])]
print(max(ma),min(mi))
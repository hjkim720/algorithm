import sys
input=sys.stdin.readline
N,L=map(int,input().split())
puddle=[]
for _ in range(N):
    puddle.append(list(map(int, input().split())))
puddle.sort()
last=0
cnt=0
for items in puddle:
    s,e=items[0],items[1]
    if last>s:
        s=last
    while s<e:
        s+=L
        cnt+=1
    last=s
print(cnt)

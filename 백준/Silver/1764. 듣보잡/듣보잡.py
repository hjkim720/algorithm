N,M = map(int,input().split())
cnt=0
D=set()
B=set()
for i in range(N):
    D.add(input())
for j in range(M):
    B.add(input())
res=sorted(list(D.intersection(B)))
print(len(res))
for items in res:
    print(items)
N,K=map(int,input().split())
table=[i for i in range(1,N+1)]
modulo=N
tmp=0
res=[]
for i in range(N):
    tmp=(tmp+K-1)%modulo
    a=table.pop(tmp)
    modulo-=1
    res.append(a)
print('<',end='')
print(*res,sep=', ',end='')
print('>')


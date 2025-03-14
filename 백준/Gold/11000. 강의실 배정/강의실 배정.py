N=int(input())
start,end=[],[]
for _ in range(N):
    a,b=map(int,input().split())
    start.append(a)
    end.append(b)
start.sort()
end.sort()
s_index=0
e_index=0
res=0
tmp=0
while s_index<N:
     if start[s_index]<end[e_index]:
         tmp+=1
         if tmp>res:
             res=tmp
         s_index+=1
     else:
        e_index+=1
        tmp-=1
print(res)



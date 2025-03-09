N=int(input())
lst=[]
for i in range(N):
    lst.append(int(input()))

i=N-1
cnt=0
while i>=1:
    if lst[i]<=lst[i-1]:
        cnt+=lst[i-1]-lst[i]+1
        lst[i-1]=lst[i]-1
    i-=1
print(cnt)
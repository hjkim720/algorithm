N=int(input())
lst=list(map(int,input().split()))
lst.sort()
start=0
end=N-1
cur_sum=abs(lst[start]+lst[end])
solution=(lst[start],lst[end])
while start<end:
    s,e=lst[start],lst[end]
    if abs(s+e)<cur_sum:
        cur_sum=abs(s+e)
        solution=(s,e)
        if cur_sum==0:
            break
    if s+e<0:
        start+=1
    else:
        end-=1
print(*solution)



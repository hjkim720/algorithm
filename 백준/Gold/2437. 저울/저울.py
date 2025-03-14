N=int(input())
lst=list(map(int,input().split()))
lst.sort()
tmp=1
for items in lst:
    if tmp<items:
        break
    tmp+=items
print(tmp)
N=int(input())
lst=[]
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
lst.sort(key=lambda x:(x[1],x[0]))
for items in lst:
    print(*items)
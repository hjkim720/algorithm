N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
rank_lst=[1]*N
for i in range(N):
    for j in range(i,N):
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            rank_lst[i]+=1
    for k in range(0,i):
        if lst[i][0]<lst[k][0] and lst[i][1]<lst[k][1]:
            rank_lst[i]+=1
print(*rank_lst)
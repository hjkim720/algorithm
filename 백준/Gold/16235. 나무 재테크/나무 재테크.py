import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
robot=list(list(map(int,input().split())) for _ in range(N))
trees=[[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i,j,age=map(int,input().split())
    trees[i-1][j-1].append(age)
food=[[5]*N for _ in range(N)]
years=1
dir=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
while years<=K:
    cnt=0
    years+=1
    tmp=[[0]*N for _ in range(N)]
    # spring
    for i in range(N):
        for j in range(N):
            trees[i][j].sort()
            will_die=[]
            for k in range(len(trees[i][j])):
                if trees[i][j][k]>food[i][j]:
                    tmp[i][j]+=trees[i][j][k]//2
                    will_die.append(trees[i][j][k])
                else:
                    food[i][j]-=trees[i][j][k]
                    trees[i][j][k]+=1
            for tree in will_die:
                trees[i][j].remove(tree)

    # summer
    for i in range(N):
        for j in range(N):
            food[i][j]+=tmp[i][j]
    # autumn
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age%5==0:
                    for d in dir:
                        wi,wj=i+d[0],j+d[1]
                        if 0<=wi<N and 0<=wj<N:
                            trees[wi][wj].append(1)
    # winter
    for i in range(N):
        for j in range(N):
            food[i][j]+=robot[i][j]
            cnt+=len(trees[i][j])

print(cnt)

import sys
from collections import deque
input=sys.stdin.readline
dic={'L':(0,-1),
     'R':(0,1),
     'U':(-1,0),
     'D':(1,0)}
# 이 문제는 사이클의 수를 찾는 문제
def go(si,sj):
    global v
    global c
    v_coor=[(si,sj)]
    q=deque()
    q.append((si,sj))
    v[si][sj]=c
    while q:
        ti,tj=q.popleft()
        d=dic[maze[ti][tj]]
        wi,wj=ti+d[0],tj+d[1]
        if v[wi][wj]==0:
            q.append((wi,wj))
            v[wi][wj]=c
            v_coor.append((wi,wj))
        elif v[wi][wj]==c:
            c+=1
            return
        else:
            a=v[wi][wj]
            for coor in v_coor:
                v[coor[0]][coor[1]]=a
            return



N,M=map(int,input().split())
v=[[0]*M for _ in range(N)]
c=1
maze=[list(map(str,input().rstrip())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if v[i][j]==0:
            go(i,j)

print(c-1)
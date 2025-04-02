import sys
sys.setrecursionlimit(800000)
input=sys.stdin.readline
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    ref_x, ref_y = find(x), find(y)
    if ref_x == ref_y:
        return
    if ref_y<ref_x:
        parent[ref_x] = ref_y
    else:
        parent[ref_y] = ref_x

N, Q = map(int, input().split())
parent = list(range(N + 1))
coord = []
for i in range(1, N + 1):
    x1, x2, y = map(int, input().split())
    coord.append((x1, x2, i))
coord.sort(key=lambda x:x[0])
last_x1,last_x2=coord[0][0],coord[0][1]
for i in range(1, N):
    cur_x1,cur_x2=coord[i][0],coord[i][1]
    if cur_x1<= last_x2:
        union(coord[i][2], coord[i-1][2])
        last_x2=max(cur_x2,last_x2)
    else:
        last_x1,last_x2=cur_x1,cur_x2


for _ in range(Q):
    s, e = map(int, input().split())
    print(1 if find(s) == find(e) else 0)
import sys
input = sys.stdin.readline
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    ref_x = find(x)
    ref_y = find(y)
    if ref_x == ref_y:
        return 0
    parent[ref_y] = ref_x
    return 1
N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1)) 
edges.sort()
parent = [i for i in range(N)]
total = 0
cnt = 0

for c, a, b in edges:
    if union(a, b):
        total += c
        cnt += 1
        if cnt == N-1:
            break
print(total)

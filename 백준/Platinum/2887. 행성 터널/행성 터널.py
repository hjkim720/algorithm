import sys
input = sys.stdin.readline

N = int(input())
planet = []
for i in range(N):
    x, y, z = map(int, input().split())
    planet.append((i, x, y, z))
edges = []
for axis in range(1, 4):
    planet.sort(key=lambda x: x[axis])
    for i in range(N-1):
        a, b = planet[i][0], planet[i+1][0]
        cost = abs(planet[i][axis] - planet[i+1][axis])
        edges.append((cost, a, b))
edges.sort()
parent = [i for i in range(N)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    ref_x = find(x)
    ref_y = find(y)
    if ref_x == ref_y:
        return False
    parent[ref_y] = ref_x
    return True

total = 0
cnt = 0
for cost, a, b in edges:
    if union(a, b):
        total += cost
        cnt += 1
        if cnt == N-1:
            break
print(total)

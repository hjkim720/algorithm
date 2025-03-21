def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x in truth and ref_y in truth:
        return
    if ref_x in truth:
        parent[ref_y] = ref_x
    elif ref_y in truth:
        parent[ref_x] = ref_y
    else:
        if ref_x > ref_y:
            parent[ref_y] = ref_x
        else:
            parent[ref_x] = ref_y


N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
parties = []
cnt = 0
parent = list(range(N + 1))
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])
    parties.append(party)
for party in parties:
    for i in range(len(party)):
        if find_set(party[i]) in truth:
            break
    else:
        cnt += 1
print(cnt)

import sys
input = sys.stdin.readline

n = int(input())
S, E = [], []
for _ in range(n):
    s, e = map(int, input().split())
    S.append(s); E.append(e)

S.sort()
E.sort()

i = j = 0
cur = 0
maxc = 0
ans_s = ans_e = 0
found = False
t = None


while i < n or j < n:

    if j == n or (i < n and S[i] < E[j]):
        next_t = S[i]
    else:
        next_t = E[j]


    if t is not None and t < next_t:

        if cur > maxc:
            maxc = cur
            ans_s = t
            ans_e = next_t
            found = True
        elif found and cur == maxc and ans_e == t:
            ans_e = next_t


    t = next_t
    while j < n and E[j] == t:
        cur -= 1
        j += 1
    while i < n and S[i] == t:
        cur += 1
        i += 1

print(maxc)
print(ans_s, ans_e)

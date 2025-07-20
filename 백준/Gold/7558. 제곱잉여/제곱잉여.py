T = int(input())
for tc in range(1, T+1):
    a, p = map(int, input().split())
    res = pow(a % p, (p-1)//2, p)
    if res == 1:
        ans = 1
    else:
        ans = -1
    print(f"Scenario #{tc}:")
    print(ans)
    print()
def gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = gcd(b, a % b)
    return g, y, x - (a // b) * y
N, A = map(int, input().split())
print(N - A, end=' ')
g, x, _ = gcd(A, N)
if g != 1:
    print(-1)
else:
    print(x % N)

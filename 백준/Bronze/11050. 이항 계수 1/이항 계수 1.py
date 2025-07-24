import sys
input = sys.stdin.readline
MOD = 1000000007
N, K = map(int, input().split())
fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = (fact[i-1] * i) % MOD
def inv(a):
    return pow(a, MOD-2, MOD)
n = fact[N]
d = (fact[K] * fact[N-K]) % MOD
result = (n * inv(d)) % MOD
print(result)
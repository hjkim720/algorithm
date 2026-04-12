import sys
input = sys.stdin.readline
MOD = 1_000_000_007

# 0: 정보과학관
# 1: 전산관
# 2: 미래관
# 3: 신양관
# 4: 한경직기념관
# 5: 진리관
# 6: 학생회관
# 7: 형남공학관

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

def mat_mul(a, b):
    n = 8
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue
            for j in range(n):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    return res

def mat_pow(mat, exp):
    n = 8
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1  # Identity Matrix. 초기값 위함임.

    while exp > 0:
        if exp % 2 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        exp //= 2

    return result

D = int(input())
res = mat_pow(graph, D)
print(res[0][0])
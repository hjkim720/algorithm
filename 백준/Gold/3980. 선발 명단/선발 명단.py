def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    results = []
    INF = 10**9  # disallowed(능력치 0) 자리에 줄 큰 페널티

    for _ in range(T):
        # 11명의 선수에 대한 11개 포지션 능력치 입력
        matrix = []
        for i in range(11):
            row = list(map(int, input().split()))
            # 능력치 0이면 -INF로 설정하여 배정되지 않도록 함.
            new_row = [val if val > 0 else -INF for val in row]
            matrix.append(new_row)
        n = 11

        # 헝가리안 알고리즘 (1-indexed로 내부 구현)
        # u, v: 잠재적 비용(라벨) / p: 매칭 결과 / way: 경로 추적용
        u = [0] * (n + 1)
        v = [0] * (n + 1)
        p = [0] * (n + 1)
        way = [0] * (n + 1)

        # 각 선수 i(1-indexed)를 순회하며 배정을 결정
        for i in range(1, n + 1):
            p[0] = i
            minv = [INF] * (n + 1)
            used = [False] * (n + 1)
            j0 = 0
            while True:
                used[j0] = True
                i0 = p[j0]
                delta = INF
                j1 = 0
                # 각 포지션 j (1-indexed)에 대해 최소값 갱신
                for j in range(1, n + 1):
                    if not used[j]:
                        # 여기서 cost는 -matrix[i0-1][j-1]로 변환함으로써
                        # 최대 능력치를 최소 비용 문제로 변환한다.
                        cur = -matrix[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(n + 1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            # 경로 역추적으로 배정 갱신
            while True:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
                if j0 == 0:
                    break

        # p[j] (j=1~n)는 j번 포지션에 배정된 선수(1-indexed)를 나타낸다.
        assignment = [0] * n  # assignment[i] : i번 선수(0-indexed)가 맡은 포지션 (0-indexed)
        for j in range(1, n + 1):
            assignment[p[j] - 1] = j - 1

        total = 0
        for i in range(n):
            total += matrix[i][assignment[i]]
        results.append(total)
    sys.stdout.write("\n".join(map(str, results)))
solve()

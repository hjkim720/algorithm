from collections import deque
def bfs():
    q = deque()
    q.append(N)
    visited = [10 ** 6 + 1] * (N+1)
    visited[N] = 0
    while q:
        t = q.popleft()
        if t == 1:
            return visited[t]
        if t % 3 == 0:
            w = t // 3
            if visited[w] > visited[t] + 1:
                q.append(w)
                visited[w] = visited[t] + 1
        if t % 2 == 0:
            w = t // 2
            if visited[w] > visited[t] + 1:
                q.append(w)
                visited[w] = visited[t] + 1
        w = t - 1
        if visited[w] > visited[t] + 1:
            q.append(w)
            visited[w] = visited[t] + 1

N = int(input())
print(bfs())
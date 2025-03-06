from collections import deque
def bfs(root):
    global cnt
    q=deque()
    visited=[0]*(N)
    q.append(root)
    if root==delete:
        return
    visited[root]=1
    while q:
        t=q.popleft()
        if tree[t] == [] or tree[t]==[delete]:
            cnt += 1
        for children in tree[t]:
            if children!=delete and visited[children]==0:
                q.append(children)
                visited[children]=visited[t]+1


N=int(input())
arr=list(map(int,input().split()))
delete=int(input())
cnt=0
tree=[[] for _ in range(N)]
for i in range(N):
    if arr[i]!=-1:
        tree[arr[i]].append(i)
    else:
        root=i
bfs(root)
print(cnt)
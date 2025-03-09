from collections import deque

def bfs(A, B):
    q = deque() 
    q.append((A,1))
    while q:
        num, count = q.popleft()
        
        if num == B:
            return count
        
        next1 = num * 2
        next2 = int(str(num) + "1")
        
        if next1 <= B:
            q.append((next1, count + 1))
        if next2 <= B:
            q.append((next2, count + 1))
    
    return -1 
A, B = map(int, input().split())
print(bfs(A, B))

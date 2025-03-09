from collections import deque

def bfs(A, B):
    q = deque() 
    q.append((A,0))
    while q:
        num, count = q.popleft()
        
        if num == B:
            return count
        if num%3==0:
            next1 = num//3
        else:
            next1=-1
        if num%2==0:
            next2=num//2
        else:
            next2 = -1
        next3 = num-1
        
        if next1 >= B:
            q.append((next1, count + 1))
        if next2 >= B:
            q.append((next2, count + 1))
        if next3>=B:
            q.append((next3,count + 1))
A=int(input())
print(bfs(A, 1))

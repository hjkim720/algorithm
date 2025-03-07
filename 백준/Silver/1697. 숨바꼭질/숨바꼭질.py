'''
이렇게 풀었더니 재귀 깊이 이슈가 발상함함
'''
# def rec(cur_loc,target,time):
#     global min_time
#     if cur_loc==target:
#         if time<min_time:
#             min_time=time
#         return 
#     if time>min_time:
#         return
#     rec(cur_loc-1,target,time+1)
#     rec(cur_loc+1,target,time+1)
#     rec(cur_loc*2,target,time+1)
# N,K=map(int,input().split())
# min_time=1000000000
# rec(N,K,0)
# print(min_time)
from collections import deque

N,K=map(int,input().split())
big=1000000
q=deque()
q.append(N)
dp=[1000000000]*big
dp[N]=0
flag=False
while q:
    cur=q.popleft()
    if dp[K]<dp[cur]:
        break
    for make_move in (cur-1,cur+1,cur*2):
            if 0<=make_move<big and dp[make_move]>dp[cur]+1:
                dp[make_move]=dp[cur]+1
                q.append(make_move)
        
print(dp[K])
               
           



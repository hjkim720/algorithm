# from itertools import permutations
# T=int(input())
# for testcase in range(1,T+1):
#     N=int(input())
#     operation=[]
#     a,s,m,d=map(int,input().split())
#     lst=(list(map(int,input().split())))
#     res=[]
#     for _ in range(a):
#         operation.append('+')
#     for _ in range(s):
#         operation.append('-')
#     for _ in range(m):
#         operation.append('*')
#     for _ in range(d):
#         operation.append('/')
#     for items in set(permutations(operation,len(operation))):
#         tmp=lst[:]
#         for i in range(len(items)):
#             if items[i]=='+':
#                 tmp[i+1]=tmp[i]+tmp[i+1]
#             elif items[i]=='-':
#                 tmp[i+1]=tmp[i]-tmp[i+1]
#             elif items[i]=='/':
#                     tmp[i+1]=int(tmp[i]/tmp[i+1])
#             else:
#                 tmp[i+1]=tmp[i]*tmp[i+1]
#         res.append(tmp[i+1])
#     print(f'#{testcase} {max(res)-min(res)}')
def dfs(depth, total, add, sub, mul, div):
    global min_res, max_res

    if depth == N:
        min_res = min(min_res, total)
        max_res = max(max_res, total)
        return

    if add:
        dfs(depth + 1, total + lst[depth], add - 1, sub, mul, div)
    if sub:
        dfs(depth + 1, total - lst[depth], add, sub - 1, mul, div)
    if mul:
        dfs(depth + 1, total * lst[depth], add, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / lst[depth]), add, sub, mul, div - 1)

T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    a, s, m, d = map(int, input().split())
    lst = list(map(int, input().split()))

    min_res = 10000000000

    max_res = -10000000000

    # DFS 시작
    dfs(1, lst[0], a, s, m, d)

    print(f'#{testcase} {max_res - min_res}')

import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    lst=list((input().strip()) for _ in range(N))
    lst.sort()
    for i in range(N-1):
        if lst[i+1].startswith(lst[i]):
            print("NO")
            break
    else:
        print("YES")
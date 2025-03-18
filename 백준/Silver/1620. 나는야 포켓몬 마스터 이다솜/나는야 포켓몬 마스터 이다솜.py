import sys
input=sys.stdin.readline
N,M=map(int,input().split())
inventory=[]
for _ in range(N):
    inventory.append(input())
for _ in range(M):
    a=input()
    try:
        a=int(a)
        print(inventory[a-1].strip())
    except:
        print(inventory.index(a)+1)
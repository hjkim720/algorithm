N=int(input())
lst=set(map(int,input().split()))
M=int(input())
arr=list(map(int,input().split()))
for num in arr:
    if num in lst:
        print(1)
    else:
        print(0)
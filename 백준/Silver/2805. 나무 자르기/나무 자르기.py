import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=list(map(int,input().split()))
start, end = 1, max(lst)  
#이진탐색을 떠올리지 못해 시간초과가 난 나...
while start <= end:
    tmp = 0
    mid = (start + end) // 2  

    for tree_hight in lst:
        if tree_hight > mid:
            tmp += tree_hight - mid 
    if tmp < M:  
        end = mid - 1  
    else:  
        start = mid + 1  

print(end)  


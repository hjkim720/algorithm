from itertools import combinations
while 1:
    lst=list(map(int,input().split()))
    if lst==[0]:
        break
    else:
        lst=lst[1:]
        for cases in combinations(lst,6):
            print(*cases)
    print()

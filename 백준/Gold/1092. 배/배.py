import sys
input=sys.stdin.readline
N=int(input())
max_weight=list(map(int,input().split()))
M=int(input())
boxes=list(map(int,input().split()))
max_weight.sort(reverse=True)
boxes.sort(reverse=True)
cnt=0
if max_weight[0]<boxes[0]:
    cnt-=1
else:
    while boxes:
        for i in range(N):
            for box in boxes:
                if box<=max_weight[i]:
                    boxes.remove(box)
                    break
        cnt+=1
print(cnt)

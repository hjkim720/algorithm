N=int(input())
cnt=0
for i in range(N):
    tmp=int(input())
    if tmp==1:
        cnt+=1
if cnt>N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
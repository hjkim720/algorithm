T=int(input())
for testcase in range(1,T+1):
    a,b,c=map(int,input().split())
    cnt=0
    while b!=0 and c!=0 and b>=c:
        b-=1
        cnt+=1
    if b<=0:
        print(f'#{testcase} {-1}')
        continue
    while a!=0 and b!=0 and a>=b:
        a-=1
        cnt+=1
    if a<=0:
        print(f'#{testcase} {-1}')
        continue
    print(f'#{testcase} {cnt}')

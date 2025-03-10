dic={}
N,M=map(int,input().split())
for i in range(N):
    link,pwd=input().split()
    dic[link]=pwd
for j in range(M):
    print (dic[input()])
from math import sqrt
import sys
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    ref_x,ref_y=find(x),find(y)
    if ref_x==ref_y:
        return
    if ref_x>ref_y:
        parent[ref_x]=ref_y
    else:
        parent[ref_y]=ref_x
N=int(input())
parent=list(range(N+1))
coord={}
for k in range(1,N+1):
    x,y=map(float,input().split())
    coord[k]=(x,y)
graph=[]
for i in range(1,N):
    for j in range(i+1,N+1):
        graph.append((i,j,sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2)))
graph.sort(key=lambda x:x[2])
res=0
cnt=0
for s,e,w in graph:
    if find(s)==find(e):
        continue
    union(s,e)
    res+=w
    cnt+=1
    if cnt==N-1:
        break
print(res)

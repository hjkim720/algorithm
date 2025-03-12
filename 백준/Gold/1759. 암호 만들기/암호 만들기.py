M,N=map(int,input().split())
lst=list(map(str,input().split()))
lst.sort()
res=[]
visited={}
final=[]
for items in lst:
    visited[items]=0
def perm(cnt):
    if cnt==M:
        v_count=0
        c_count=0
        for i in range(len(res)):
            if res[i] in ('a','e','i','o','u'):
                v_count+=1
            else:
                c_count+=1
        if v_count>=1 and c_count>=2:
            print(''.join(res))
        return



        return
    for items in lst:
        if not visited[items]:
            if res:
                if lst.index(items)>lst.index(res[-1]):
                    visited[items]=1
                    res.append(items)
                    perm(cnt+1)
                    res.pop()
                    visited[items]=0
            else:
                visited[items] = 1
                res.append(items)
                perm(cnt + 1)
                res.pop()
                visited[items] = 0

perm(0)

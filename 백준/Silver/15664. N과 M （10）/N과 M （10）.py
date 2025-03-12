N,M=map(int,input().split())
lst=list(map(int,input().split()))
res=[]
lst.sort()
cnt_dic={}
final=set()
for i in lst:
    if i in cnt_dic:
        cnt_dic[i]+=1
    else:
        cnt_dic[i]=1
def perm(cnt):
    if cnt==M:
        final.add(tuple(res))
        return
    for items in lst:
        if not res:
            if cnt_dic[items]!=0:
                cnt_dic[items]-=1
                res.append(items)
                perm(cnt+1)
                res.pop()
                cnt_dic[items]+=1
        else:
            if items>=res[-1]:
                if cnt_dic[items] != 0:
                    cnt_dic[items] -= 1
                    res.append(items)
                    perm(cnt + 1)
                    res.pop()
                    cnt_dic[items] += 1

perm(0)
for items in final:
    print(*items)
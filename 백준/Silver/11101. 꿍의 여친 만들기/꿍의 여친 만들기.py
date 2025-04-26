

T=int(input())
for tc in range(T):
    time=list(map(str,input().split(',')))
    dic={}
    for items in time:
        category,num= items.split(':')
        num=int(num)
        dic[category]=num
    res=21e9
    satisfy=list(map(str,input().split('|')))

    for s in satisfy:
        tmp_lst=list(s.split('&'))
        tmp=0
        for items in tmp_lst:
            if items in dic:
                tmp=max(dic[items],tmp)
            else:
                continue
        res=min(tmp,res)
    print(res)
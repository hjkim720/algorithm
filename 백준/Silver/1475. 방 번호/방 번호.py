lst=list(map(int,input().strip()))
dic={}
for i in range(10):
    dic[i]=0
for i in range(len(lst)):
    if dic[lst[i]]<=max(dic.values()):
        if lst[i]==6 and dic[6]>dic[9]:
            dic[9]+=1
        elif lst[i]==9 and dic[6]<dic[9]:
            dic[6]+=1
        else:
            dic[lst[i]]+=1
print(max(dic.values()))

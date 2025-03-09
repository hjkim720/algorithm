a='0'+input()
lst=list(map(str,a))
cnt=0
for i in range(1,len(lst)):
    if lst[i]=='Y':
        for j in range(i,len(a),i):
            if lst[j]=='Y':
                lst[j]='N'
            else:
                lst[j]='Y'
        cnt+=1
print(cnt)
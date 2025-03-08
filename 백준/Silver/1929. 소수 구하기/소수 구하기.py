from math import floor
mini,maxi=map(int,input().split())
for i in range(mini,maxi+1):
    if i==1:
        continue
    for j in range(1,floor(i**(1/2))+1):
        if j==1:
            continue
        if i%j==0:
            break
    
    else:
        print(i)
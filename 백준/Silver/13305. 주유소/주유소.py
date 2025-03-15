N=int(input())
distance=list(map(int,input().split()))
price=list(map(int,input().split()))
res=price[0]*distance[0]
least_price=price[0]
for i in range(1,N-1):
    if price[i]<least_price:
        least_price=price[i]
    res+=least_price*distance[i]
print(res)
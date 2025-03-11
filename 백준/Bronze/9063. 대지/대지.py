T=int(input())
lst_i=[]
lst_j=[]
for _ in range(T):
    i,j = map(int,input().split())
    lst_i.append(i)
    lst_j.append(j)
def find():
    max_i=max(lst_i)
    min_i=min(lst_i)
    max_j=max(lst_j)
    min_j=min(lst_j)
    if max_i==min_i or max_j==min_j:
        return 0
    else:
        return (max_i-min_i)*(max_j-min_j)
print(find())
     
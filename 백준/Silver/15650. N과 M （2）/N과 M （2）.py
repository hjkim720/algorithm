def comb(current_index,current_set):
    if len(current_set)==M:
        print(*current_set)
        return
    if current_index<N:
        current_set.append(n[current_index])
        comb(current_index+1,current_set)
        current_set.pop()
        comb(current_index+1,current_set)
N,M=map(int,input().split())
n=range(1,N+1)
comb(0,[])

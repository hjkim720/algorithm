N = int(input())
lst_1=list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

lst_1.sort()
lst_2.sort(reverse=True)

res = 0
for i in range(N):
    res += lst_1[i] * lst_2[i]

print(res)
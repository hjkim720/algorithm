res=0
for _ in range(5):
    tmp=40
    n=int(input())
    if n>40:
        tmp=n
    res+=tmp
print(res//5)
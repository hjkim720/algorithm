r=int(input())
c=int(input())
lst=['*'*c for _ in range(r)]
print(*lst,sep='\n')
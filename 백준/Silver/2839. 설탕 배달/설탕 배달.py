'''
3*x + 5*y = N
y= (N-3*x)//5
x + y = x+(N-3*x)//5 의 최소
'''
N = int(input())
result=[]
max_x = N//3
if max_x==0:
    print(-1)
    
else:

    for x in range(max_x+1):
        if 3*x+5*((N-3*x)//5) == N:
            result.append(x+(N-3*x)//5)
    if len(result):
        print(min(result))
    else:
        print(-1)
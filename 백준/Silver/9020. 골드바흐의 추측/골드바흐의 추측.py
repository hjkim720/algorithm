def is_prime(n):
    if n==1:
        return 'No'
    elif n==2:
        return 'Yes'
    for i in range(2,int(n**(1/2))+1):
        if n % i ==0:
            return 'No'
    return 'Yes'

N=int(input())
for _ in range(N):
    num=int(input())
    #덧셈이니 일단 반으로 갈라보자
    decrease=num//2
    increase=num//2
    for _ in range(num//2):
        if is_prime(decrease)=='Yes' and is_prime(increase)=='Yes':
            print(decrease,increase)
            break
        #안된다면 1 증가, 1감소 시켜줌->더한 값은 계속 N
        else:
            decrease-=1
            increase+=1

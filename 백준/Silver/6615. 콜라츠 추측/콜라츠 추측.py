def collatz(number,res):
    res.append(number)
    if number==1:
        return res
    if number%2:
        return collatz(3*number+1,res)
    else:
        return collatz(number//2,res)
while True:
    A,B=map(int,input().split())
    if A==0 and B==0:
        break
    a=collatz(A,[])
    b=collatz(B,[])
    for items in a:
        if items in b:
            print(f'{A} needs {a.index(items)} steps, {B} needs {b.index(items)} steps, they meet at {items}')
            break
    

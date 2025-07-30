lst=list(int(input()) for _ in range(3))
if sum(lst) != 180: print('Error')
else:
    if lst[0]==60 and lst[1]==60 and lst[2]==60:
        print('Equilateral')
    elif lst[0]==lst[2] or lst[1]==lst[2] or lst[0]==lst[1]:
        print('Isosceles')
    else: print('Scalene')
T=int(input())
for testcase in range(T):
    lst=list(map(str,input()))
    stack=[]
    for i in range(len(lst)):
        if lst[i]=='(':
            stack.append('(')
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack):
            print('NO')
        else:
            print('YES')
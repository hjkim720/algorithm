lst = list(input())
stack = []
res = 0

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')
    else:  # ')'
        stack.pop()
        if lst[i - 1] == '(':  # 레이저
            res += len(stack)
        else:  # 막대기의 끝
            res += 1

print(res)

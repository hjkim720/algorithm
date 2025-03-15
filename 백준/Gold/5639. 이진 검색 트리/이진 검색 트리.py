import sys
sys.setrecursionlimit(10**4)
lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

left = {}
right = {}

stack = [lst[0]]  # root
for i in range(1, len(lst)):
    node = lst[i]
    parent = None
    # 부모를 찾아서서
    while stack and stack[-1] < node:
        parent = stack.pop()

    if parent: 
        right[parent] = node
    else: 
        left[stack[-1]] = node

    stack.append(node)  


def postorder(node):
    if node is None:
        return
    if node in left:
        postorder(left[node])
    if node in right:
        postorder(right[node])
    print(node)

postorder(lst[0])

def pre_order(point):
    global pre_result
    if point:
        pre_result+=point
        pre_order(left[point])
        pre_order(right[point])
def in_order(point):
    global in_result
    if point:
        in_order(left[point])
        in_result+=point
        in_order(right[point])
def post_order(point):
    global post_result
    if point:
        post_order(left[point])
        post_order(right[point])
        post_result+=point
        



pre_result=''
in_result=''
post_result=''

N=int(input())
left={}
right={}
for _ in range(N):
    p,l,r= map(str, input().split())
    if l=='.' and r!='.':
        left[p]=0
        right[p]=r
    elif l!='.' and r=='.':
        left[p]=l
        right[p]=0
    elif l=='.' and r=='.':
        left[p]=0
        right[p]=0
    else: 
        left[p]=l

        right[p]=r
   
pre_order('A')
print(pre_result)
in_order('A')
print(in_result)
post_order('A')
print(post_result)
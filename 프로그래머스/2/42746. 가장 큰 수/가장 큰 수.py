def solution(numbers):
    answer = ''
    lst=list(map(str,numbers))
    lst.sort(key=lambda x: x*3,reverse=True)
    if lst[0]=="0":
        return "0"
    answer=''.join(lst)
    return answer
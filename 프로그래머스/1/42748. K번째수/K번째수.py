def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k=command
        lst=array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
    return answer
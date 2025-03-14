import sys

N = int(sys.stdin.readline()) 
count = [0] * 10001  
# 입력 값을 카운트 배열에 저장
for _ in range(N):
    count[int(sys.stdin.readline())] += 1

# 결과 출력
for num in range(10001 ):
    if count[num] > 0:
        for _ in range(count[num]):
            print(num)

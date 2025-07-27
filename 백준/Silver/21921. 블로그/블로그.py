import sys
input=sys.stdin.readline
N, X = map(int, input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[:X])
max_sum = window_sum
count = 1

for i in range(X, N):
    window_sum += arr[i] - arr[i-X]
    if window_sum > max_sum:
        max_sum = window_sum
        count = 1
    elif window_sum == max_sum:
        count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)

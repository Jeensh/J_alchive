import sys
input = sys.stdin.readline

# 입력 받기
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

# 자연수들 내림차순으로 정렬
numbers.sort()
numbers.reverse()

# 결과 구하기
result = 0
count = 0
MAX = numbers[0]
for i in range(1, M + 1):
    count += 1
    if count == K + 1 or numbers[0] < MAX:
        count = 1
        numbers[0], numbers[1] = numbers[1], numbers[0]
    result += numbers[0]

# 결과 출력
print(result)
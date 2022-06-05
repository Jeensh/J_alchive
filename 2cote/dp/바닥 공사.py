# 가로 길이 N 입력받기
n = int(input())

# dp 테이블 초기화
array = [0] * 1001

# 경우의 수 찾기(바텀 업)
count = 0
array[1] = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        array[i] = (array[i - 1] * 2) + 1
    else:
        array[i] = (array[i - 1] * 2) - 1

# 출력
print(array[n] % 796796)
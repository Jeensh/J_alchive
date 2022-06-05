# 일직선의 식량 창고 개수 N입력받기
n = int(input())

# 식량 창고 별 식량 개수 입력받기
data = list(map(int, input().split()))

MAX = 0
def solve(i, sum):
    global n, MAX
    sum += data[i]
    if i >= n - 2:
        MAX = max(MAX, sum)
    else:
        for k in range(2, n - i):
            solve(i + k, sum)

# 출력
for j in range(0, n):
    solve(j, 0)
print(MAX)
# n + 1일 째 되는날 퇴사
# 남은 n일 동안 최대한 많은 상담

# n 입력받기
n = int(input())

# 정보 입력받기
data = [(0, 0)]
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))


dp = [0] * (n + 1)
result = 0
# 알고리즘 수행
# 선택하고 진행하는 것과 선택하지 않고 진행하는 것으로 매상황 진행
def solve(day, total, n):
    global result
    if day > n + 1:
        return
    if day == n + 1:
        result = max(result, total)
        return
    # 오늘 상담을 진행하는 경우
    t, p = data[day]
    solve(day + t, total + p, n)
    # 오늘 상담을 진행하지 않는 경우
    solve(day + 1, total, n)

solve(1, 0, n)
print(result)
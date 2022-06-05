# N, M 입력받기
n, m = map(int, input().split())
# 각 화폐의 가치 입력받기
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

# 다이나믹 프로그래밍 진행(탑 다운)
MIN = 9999
def solve(i, count):
    global MIN
    if count >= MIN or i < 0:
        return
    elif i == 0:
        MIN = min(MIN, count)
    else:
        for d in data:
            solve(i - d, count + 1)

solve(m, 0)
if MIN == 9999:
    MIN = -1
print(MIN)
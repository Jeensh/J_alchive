import sys
input = sys.stdin.readline

# 입력 받기
row, col = map(int, input().split())
data = []
for i in range(row):
    data.append(list(map(int, input().split())))

# 각 행을 참조하면서 해당 행에서 가장 작은 수와 MAX를 비교하여 더 큰 수를 MAX에 넣기
MAX = 0
for r in data:
    MAX = max(min(r), MAX)

# 결과 출력
print(MAX)
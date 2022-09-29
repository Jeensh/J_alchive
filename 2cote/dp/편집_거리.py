# 출발 문자열 입력받기
from re import A


s = list(input())
# 도착 문자열 입력받기
target = list(input())

n = len(s)
m = len(target)

dp = [[0] * (m + 1) for i in range(n + 1)]

# 출발 문자열이 빈 문자열인 경우와 도착 문자열이 빈 문자열인 경우 dp 테이블 갱신
for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j

# dp 테이블 전부 갱신하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 두 문자가 같은 경우
        # 해당 문자를 제외한 나머지 문자열을 같게 만드는데 들었던 편집거리를 그대로 가져옴[i -1][j -1](왼쪽 위)
        if s[i - 1] == target[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        # 두 문자가 다른 경우
        # 3가지 경우 중 가장 작은 것 + 1
        # 삽입 : (왼쪽) dp[i][j - 1]의 값은 target의 해당 문자를 제외한 문자열을 s의 문자열로 만드는 최소 편집 수
        # 교체 : (왼쪽위) dp[i -1][j - 1]의 값은 target의 해당 문자를 제외한 문자열을 s의 해당 문자를 제외한 문자열로 만드는 최소 편집의 수
        # 삭제 : (위쪽) dp[i - 1][j]의 값은 target을 해당 문자를 포함한 문자열은 s의 해당 문자를 제외한 문자열로 만드는 최소 편집의 수
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1

print(dp[n][m])

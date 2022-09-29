# 전투력이 높은 병사가 앞으로 오도록 내림차순 배치
# 배치과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 사용
# 그러면서도 남아있는 병사가 최대

# n 입력받기
n = int(input())

# 병사들 전투력 입력받기
sol = list(map(int, input().split()))

sol.reverse()

dp = [1] * n
for i in range(1, n):
    MAX_idx = -1
    for j in range(i):
        if sol[j] < sol[i]:
            if MAX_idx == -1:
                MAX_idx = j
            else:
                if dp[MAX_idx] < dp[j]:
                    MAX_idx = j
    if MAX_idx != -1:
        dp[i] = dp[MAX_idx] + 1


# print(sol)
# print(dp)
print(n - max(dp))
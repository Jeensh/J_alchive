import sys
input = sys.stdin.readline
from bisect import bisect_left
# 대회는 정확히 3명으로 구성된 팀만 참가 가능
# 코딩 실력이 좋으면 팀워크가 떨어지고, 팀워크가 좋으면 코딩 실력이 떨어짐
# 모든 학생들의 코딩 실력을 알고 있음
# 세팀원의 코딩실력의 합이 0이 되는 팀을 만들고자 함
# 대회에 출전할 수 있는 팀을 얼마나 만들 수 있는지 계산

######## 진행 ########
# n 입력받기
n = int(input())

# 코딩 실력 입력받기
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(n - 2):
    cost = data[i]
    start = i + 1
    end = n - 1
    while start < end:
        s_cost = data[start]
        e_cost = data[end]
        cost_sum = cost + s_cost + e_cost
        if cost_sum == 0:
            if s_cost == e_cost:
               result += end - start
            else:
                for t in range(end - 1, start, -1):
                    if e_cost == data[t]:
                        result += 1
                    else:
                        break
            start += 1
        elif cost_sum < 0:
            start += 1
        else:
            end -= 1

print(result)
    
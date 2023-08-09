# 특정 조건
#   - 자릿수를 기준으로 점수 N을 반으로 나누어,
#   - 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일 한 상황

n = input()
half = int(len(n) / 2)

sum1 = 0
sum2 = 0
for c in n[:half]:
    sum1 += int(c)

for c in n[half:]:
    sum2 += int(c)

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
arr = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    arr[x] += 1

result = 0
# 1부터 m까지 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= arr[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += arr[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)
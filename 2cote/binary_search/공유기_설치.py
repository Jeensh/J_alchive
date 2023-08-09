# 집 n개가 수직선 위
# 공유기 c개


# 집의 개수 n과 공유기 개수 c 입력받기
n, c = map(int, input().split())

# 집의 좌표 입력받기
data = []
for i in range(n):
    data.append(int(input()))

# 집 좌표 오름차순 정렬
data.sort()

# 찾아야 하는 것 : 공유기를 설치했을 때 가장 인접한 두 공유기 사이의 거리가 최대는 경우 두 공유기 사이의 거리
start = 1 # 두 공유기 사이의 거리의 최소값
end = data[-1] - data[0] # 두 공유기 사이의 거리의 최대값
result = 0

while start <= end:
    mid = (start + end) // 2 # 이번에 시험할 두 공유기의 거리
    last = data[0] # 앞에 있는 공유기의 좌표
    count = 1
    # 앞에서부터 공유기 설치
    for i in range(1, n):
        # 두 공유기의 거리가 기준(mid)보다 같거나 큰 경우
        if data[i] - last >= mid:
            # 공유기 설치 및 앞에 있는 공유기 좌표 갱신
            count += 1
            last = data[i]
    # 만약 설치된 공유기가 설치해야 하는 공유기 개수보다 적은 경우
    if count < c:
        # 공유기 사이의 거리의 최대값을 줄임
        end = mid - 1
    # 만약 설치된 공유기가 설치해야 하는 공유기 개수보다 크거나 같은경우
    else:
        # 공유기 사이의 거리의 최소값을 높임
        start = mid + 1
        result = mid

print(result)
# 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = list(map(int, input().split()))

# 전체 집 좌표 정보 입력받기
array = []
for _ in range(n):
    array.append(int(input()))

# 이진 탐색을 위한 정렬 수행
array.sort()

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1
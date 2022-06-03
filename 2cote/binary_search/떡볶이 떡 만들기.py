# 떡의 개수 N과 요청한 떡의 길이 M을 입력받기
n, m = map(int, input().split())
# M개의 떡 길이 입력받아 리스트에 넣기
data = list(map(int, input().split()))

# 가장 긴 떡의 길이로 절단기 높이 초기화
cut = max(data)

# 절단기 높이를 1씩 줄이면서 잘린 떡의 합이 요청한 떡의 길이와 같거나 커질때 해당 높이 출력
while True:
    cutted = 0
    for d in data:
        if d - cut > 0:
            cutted += d - cut
    if cutted >= m:
        print(cut)
        break
    cut -= 1
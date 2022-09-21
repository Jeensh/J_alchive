# 인원수 N 입력받기
n = int(input())

# 공포도 입력받기
fearRate = list(map(int, input().split()))

# 공포도가 낮은 순으로 정렬
fearRate.sort()

# 채워야 하는 공포도
need = 0
# 현재 멤버 수
member = 0
# 만들어진 그룹
result = 0
# 공포도가 낮은 사람부터 그룹을 만들어감
for i in fearRate:
    need = max(need, i)
    member += 1
    if need <= member:
        result += 1
        member = 0

# 결과 출력
print(result)
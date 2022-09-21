# 수 입력받기
num = input()

# 최종 결과
result = int(num[0])

# 왼쪽에서부터 연산 결과가 + or x 중 큰 것으로 선택해가면서 계산
for n in num[1:]:
    result = max(result + int(n), result * int(n))

# 출력
print(result)
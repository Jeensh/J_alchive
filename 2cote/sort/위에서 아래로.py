# 수열에 속해있는 수의 개수 N 입력받기
n = int(input())

# 수열에 속해있는 수 입력 받기
num_list = []
for i in range(n):
    num_list.append(int(input()))

# 오름차순 정렬
num_list.sort()
# 거꾸로 바꾸어 내림차순 정렬
num_list.reverse()

# 결과 출력
for num in num_list:
    print(num, end = ' ')

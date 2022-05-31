# 학생의 수 N 입력받기
n = int(input())

# 학생 정보 입력받기 "홍길동 95" -> "이름 성적"
data = []
for i in range(n):
    name, grade = input().split()
    data.append((int(grade), name))

# 정렬 하기
data.sort()

# 출력하기
for d in data:
    print(d[1], end=" ")
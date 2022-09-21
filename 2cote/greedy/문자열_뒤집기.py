# 문자열 s 입력받기
s = input()

# 모두 0으로 통일하는 경우
tmp = list(s.split('1'))
result1 = [i for i in tmp if i != '']

# 모드 1로 통일하는 경우
tmp = list(s.split('0'))
result2 = [i for i in tmp if i != '']

print(min(len(result1), len(result2)))
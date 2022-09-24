from itertools import count

# u, v로 분리하기
def divide(p):
    count_left = 0
    count_right= 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == '(':
            count_left += 1
        elif p[i] == ')':
            count_right += 1
        u += p[i]
        if count_left == count_right:
            for j in range(i + 1, len(p)):
                v += p[j]
            break
    return (u, v)

# 올바른 괄호 문자열인지 확인
def check(p):
    count_left = 0
    count_right = 0
    for i in range(len(p)):
        if p[i] == '(':
            count_left += 1
        elif p[i] == ')':
            count_right += 1
        if count_right > count_left:
            return False
    return True

def solution(p):
    answer = ''

    # 빈 문자열인 경우 그대로 반환
    if len(p) == 0:
        return p

    # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    # 단, u는 "균형잡힌 괄호 문자열"로 더이상 분리할 수 없어야 하며
    # v는 빈 문자열이 될 수 있음
    u, v = divide(p)

    # 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행
    if check(u):
        if check(v):
            return u + v
        else:
            return u + solution(v)
    # 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정 수행
    else:
        # 빈 문자열에 첫번째 문자로 '('를 붙임
        tmp = "("
        # 문자열 ㅍ에 대해 1단계 부터 재귀적으로 수행한 결과 문자열을 이어 붙임
        tmp += solution(v)
        # ')'를 다시 붙임
        tmp += ")"
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        u = u[1 : len(u) - 1]
        new_u = ""
        for c in u:
            if c == '(':
                new_u += ')'
            elif c == ')':
                new_u += '('
        tmp += new_u
        return tmp

print(solution("()))((()"))
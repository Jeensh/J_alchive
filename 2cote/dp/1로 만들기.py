# 정수 X 입력받기
x = int(input())

MIN = 9999
# 최소의 수 찾기
def solve(n, count):
    global MIN
    if n == 1:
        MIN = min(MIN, count)
    elif count > MIN:
        return
    else:
        if n % 5 == 0:
            solve(n / 5, count + 1)
        if n % 3 == 0:
            solve(n / 3, count + 1)
        if n % 2 == 0:
            solve(n / 2, count + 1)
        solve(n - 1, count + 1)

# 답 구하고 출력하기
solve(x, 0)
print(MIN)
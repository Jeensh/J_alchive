import sys
input = sys.stdin.readline

# 수의 개수 n 입력받기
n = int(input())

# 수 입력받기
nums = list(map(int, input().split()))

# 연산자 입력받기
# 연산자 + - x /
op = list(map(int, input().split()))

# 순열 함수
def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            tmp = [i for i in arr]
            tmp.remove(arr[i])
            for j in perm(tmp, n - 1):
                if [arr[i]] + j not in result:
                    result.append([arr[i]] + j)
    return result

# 연산자를 리스트 안에 넣기
# 0, 1, 2, 3 : + - * /
op_list = []
for i in range(4):
    tmp = [i] * op[i]
    op_list += tmp
op_perm = perm(op_list, len(op_list))

# # 중복 없애기
# for i in range(len(op_perm)):
#     op_perm[i] = tuple(op_perm[i])
# op_perm = set(op_perm)
# op_perm = list(op_perm)
# print(op_perm)

# 각 순열마다 값을 구하여 최대값과 최소값 구하기
MIN = 1000000000
MAX = -1000000000
for o in op_perm:
    res = nums[0]
    for i in range(len(o)):
        if o[i] == 0:
            res += nums[i + 1]
        elif o[i] == 1:
            res -= nums[i + 1]
        elif o[i] == 2:
            res *= nums[i + 1]
        elif o[i] == 3:
            if res < 0 and nums[i + 1] > 0:
                res *= -1
                res = res // nums[i + 1]
                res *= -1
            else:
                res = res // nums[i + 1]
    MIN = min(MIN, res)
    MAX = max(MAX, res)

# 출력
print(MAX)
print(MIN)
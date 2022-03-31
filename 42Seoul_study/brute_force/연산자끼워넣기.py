import sys
input = sys.stdin.readline
from collections import deque

# 최대, 최소 값 초기화
MAX = -1000000000
MIN = 1000000000

def cal(num1, num2, op):
	if op == '+':
		return num1 + num2
	if op == '-':
		return num1 - num2
	if op == '*':
		return num1 * num2
	if op == '/':
		return int(num1 / num2)

def sol(nums, add, sub, mul, div, dept):
	global MAX, MIN
	if dept == N - 1:
		MAX = max(nums[0], MAX)
		MIN = min(nums[0], MIN)
		return
	if add > 0:
		nums_l = deque(nums)
		num1 = nums_l.popleft()
		num2 = nums_l.popleft()
		nums_l.appendleft(cal(num1, num2, '+'))
		sol(nums_l, add - 1, sub, mul, div, dept + 1)
	if sub > 0:
		nums_l = deque(nums)
		num1 = nums_l.popleft()
		num2 = nums_l.popleft()
		nums_l.appendleft(cal(num1, num2, '-'))
		sol(nums_l, add, sub - 1, mul, div, dept + 1)
	if mul > 0:
		nums_l = deque(nums)
		num1 = nums_l.popleft()
		num2 = nums_l.popleft()
		nums_l.appendleft(cal(num1, num2, '*'))
		sol(nums_l, add, sub, mul - 1, div, dept + 1)
	if div > 0:
		nums_l = deque(nums)
		num1 = nums_l.popleft()
		num2 = nums_l.popleft()
		nums_l.appendleft(cal(num1, num2, '/'))
		sol(nums_l, add, sub, mul, div - 1, dept + 1)


if __name__ == "__main__":
	# 입력 받기
	N = int(input())
	nums = list(map(int, input().strip().split()))
	tmp = list(map(int, input().strip().split()))
	ops = {'+' : tmp[0], '-' : tmp[1], '*' : tmp[2], '/' : tmp[3]}

	# 최대, 최소 값 구하기
	sol(nums, ops['+'], ops['-'], ops['*'], ops['/'], 0)
	# print(dup_list)
	print(MAX)
	print(MIN)

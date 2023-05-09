# 8개의 톱니를 가지고 있는 톱니바퀴 4개
# 톱니는 S or N극
# 가장 왼쪽 톱니바퀴가 1번, 가장 왼쪽이 4번

# 톱니바퀴를 총 k번 회전
# 회전은 시계방향과 반시계 방향이 있음

# 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라 옆에 있는 톱니바퀴를 회전시킬수도 아닐 수도 있다
# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면 B는 A와 반대 방향으로 회전한다
#   - 맞닿은 톱니의 극이 같다면 회전하지 않는다

# 맞닿은 톱니 번호
# 1, 2 : (3, 9)
# 2, 3 : (3, 9)
# 3, 4 : (3, 9)

# 톱니 회전시키기
def spin(gears, i, d, spined):
    if i in spined:
        return
    spined.append(i)
    left = gears[i][6]
    right = gears[i][2]
    # 선택한 톱니바퀴의의 오른쪽 녀석이 회전할 녀석이면 회전
    if i + 1 <= 4 and gears[i + 1][6] != right:
        spin(gears, i + 1, -d, spined)
    # 선택한 톱니바퀴의 왼쪽 녀석이 회전할 녀석이면 회전
    if i - 1 > 0 and gears[i - 1][2] != left:
        spin(gears, i - 1, -d, spined)
    # 본인 회전
    if d == 1:
        tmp = gears[i][-1]
        del gears[i][-1]
        gears[i].insert(0, tmp)
    else:
        tmp = gears[i][0]
        del gears[i][0]
        gears[i].append(tmp)


# 각 톱니바퀴의 상태 입력받기
gears = [[]]
for i in range(4):
    s = input()
    tmp = []
    for c in s:
        tmp.append(int(c))
    gears.append(tmp)

# 회전 횟수 k 입력받기
k = int(input())

# 회전시킬 톱니의 번호화 방향 입력받기(1 : 시계 방향, -1 : 반시계 방향)
step = []
for i in range(k):
    a, b = map(int, input().split())
    step.append((a, b))

# 진행
for i, d in step:
    spin(gears, i, d, [])

# 점수 합 구하기
result = 0
if gears[1][0] == 1:
    # print('a')
    result += 1
if gears[2][0] == 1:
    # print('b')
    result += 2
if gears[3][0] == 1:
    # print('c')
    result += 4
if gears[4][0] == 1:
    # print('d')
    result += 8

print(result)
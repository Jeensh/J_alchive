# N + 1일째 되는날 퇴사할 때 N 입력받기
N = int(input())

# Ti, Pi 입력받기
data = [0]
for i in range(N):
    a, b = map(int, input().split())
    data.append((a, b))

# 스케줄표 만들기
schedule = [0 for i in range(N + 1)]

# 최대 이익
MAX = 0

def solve(schedule, day, earn):
    global MAX
    schedule_l = schedule[:]
    if day == N + 1:
        MAX = max(earn, MAX)
        return
    # 오늘 들어온 상담을 시작하려는 경우
    for i in range(day, day + data[day][0]):
        # 상담이 가능한지 확인
        if i > N or schedule_l[i] == 1:	# 이미 스케줄이 차있거나, 퇴사기한을 넘긴다면
            solve(schedule_l, day + 1, earn) # 다음날로 넘어가기
            return
    # 상담이 가능하다면
    earn_l = earn + data[day][1]	# 돈을 받고
    for i in range(day, day + data[day][0]):	# 스케줄 적용
        schedule_l[i] = 1
    solve(schedule_l, day + 1, earn_l)

    # 오늘 들어온 상담을 넘기는 경우
    schedule_l = schedule[:]
    solve(schedule_l, day + 1, earn)

solve(schedule, 1, 0)
print(MAX)
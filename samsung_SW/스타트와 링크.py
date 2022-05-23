# N(짝수) 입력받기
N = int(input())
members = set()
for i in range(N):
    members.add(i)

# 능력치 보드 입력받기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 팀 능력치 구하기
def get_team_power(board, team):
    power = 0
    number = len(team)
    for i in team:
        for j in team:
            if j == i:
                continue
            power += board[i][j]
    return power

gap = 10000000

def solve(board, team1):
    global N, gap, members
    if len(team1) == N / 2:
        team2 = members - team1
        power_team1 = get_team_power(board, team1)
        power_team2 = get_team_power(board, team2)
        gap = min(gap, abs(power_team1 - power_team2))
        return
    if not team1:
        start = 0
    else:
        start = max(team1)
    for i in range(start, N):
        if not team1 and i > 0:
            return
        team_l = set(team1)
        if i in team1:
            continue
        team_l.add(i)
        solve(board, team_l)

solve(board, [])
print(gap)
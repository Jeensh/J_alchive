# 참고: https://github.com/cpm0722/kakao-2022-round2/blob/master/http_json.py
import requests

# http 요청
def http_method(method : str, base_url : str, sub_url : str, data={}, token="", init = False):
    assert method in ["GET", "POST", "PUT"]
    headers = {}
    headers['Accept'] = "application/json"
    headers['Content_Type'] = "application/json"
    if init is True:
        headers['X-Auth-Token'] = token
    else:
        headers['Authorization'] = token

    if method == "GET":
        response = requests.get(base_url+sub_url, headers=headers)
    elif method == "POST":
        response = requests.post(base_url+sub_url, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(base_url+sub_url, headers=headers, json=data)
    else:
        return {}
    status_code = response.status_code
    res = {}
    if status_code == 200:
        res = response.json()
    return res

# 시작
# auth-key 획득하기 위함
def start_api(url, token, problem_num):
    if problem_num == 1:
        data = {"problem" : 1}
    else:
        data = {"problem" : 2}
    return http_method("POST", url, '/start', data = data, token = token, init = True)

# NewRequest
# 현재 날짜에 새로 들어온 예약 요청을 받기 위함
# id(예약 요청 id), amount(객실 수), check_in_date(체크인 날짜), check_out_date(체크아웃 날짜)
def new_requests(url, key):
    response = http_method("GET", url, '/new_requests', token = key, init = False)
    return response['reservations_info']

# Reply
# 특정 예약 요청에 대한 승낙 / 거절을 답변하기 위함
# reply_list : [{ "id": 412424, "reply": "accepted"}, { "id": 707981, "reply": "refused"}]
def reply(url, key, reply_list):
    data = {'replies' : reply_list}
    response = http_method("PUT", url, '/reply', data = data, token = key, init = False)
    if not response:
        print("reply Failed!!")

# Simulate
# 오늘 호텔에 체크인 하려는 손님들에게 객실 번호를 배정해 서버에 전달하고 1일이 진행됨
# 현재 날짜가(시나리오의 최대 날짜)일 때 api를 호출하면 시뮬레이션이 종료됨
# 호출시 다음과 같은 일 진행
#   1. 응시자에게 전달받은 순서대로 객실을 배정
#       - (전달받은 객실 번호) ~ (전달받은 객실 번호 + 객실 수 -1)의 객실을 손님에게 배정
#       - 만약 객실이 비어있지 않거나 객실 번호의 범위가 올바르지 않다면 무시
#       - 객실을 성공적으로 배정했다면 해당 객실들은 체크아웃 날짜 전까지 사용 중인 상태가 됨
#   2. 호텔에 도착한 손님 중 객실이 배정되지 않은 손님은 객실 배정에 실패한 것으로 처리
#   3. 답변하지 않은 예약 중 답변 기한이 현재 날짜인 예약은 거절한 것으로 처리
#   4. 현재 날짜가 1일 증가
#   5. 현재 날짜에 체크아웃하는 객실들이 빈 객실이 됨
#   6. 현재 날짜에 체크인 하는 손님들이 호텔에 도착
#   room_assign : [{ "id": 707981, "room_number": 2023}, { "id": 975671, "room_number": 1001}]
# 1일 증가한 현재 날짜와 예약 승낙했으나 객실 배정에 실패한 횟수 반환
def simulate(url, key, room_assign):
    data = {"room_assign" : room_assign}
    response = http_method("PUT", url, '/simulate', data = data, token = key, init = False)
    print("*************************")
    print(response)
    return response

# score
# 해당 Auth key로 획득한 점수 반환
def score(url, key):
    response = http_method("GET", url, '/score', token = key, init = False)
    print(response)
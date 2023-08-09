from api import *
# 한 층에 20개의 객실이 있는 3층 건물
# 날짜 : 1 ~ 200
# 예약 요청 빈도 : 일당 요청 수 평균 1
# 각 예약 요청의 객실 수 : 1이상 10이하
# 각 예약 요청의 머무는 기간(체크아웃 날짜 - 체크인 날짜) : 1이상 20이하
# 객실 이용률 목표치 60%

TOKEN = 'cee45e1ff183ff8cbd3c65292cb05755'
URL = 'https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api'
END_DATE = 200

if __name__ == "__main__":

    response = start_api(URL, TOKEN, 1)
    auth_key = response['auth_key']

    # 예약 요청 리스트
    request_list = []
    # 오늘 날짜
    now = 1

    # 객실 예약 현황
    book = {}
    for floor in range(1, 4):
        for num in range(1, 21):
            room_number = (floor * 1000) + (num)
            book[room_number] = []

    # 날짜별 예약 현황
    reserved = {}
    for i in range(1, 201):
        reserved[i] = []

    # 진행
    while now <= END_DATE:
        reply_list = []

        # test : 진행 확인
        print('--------------------------------------------------------------------------')
        # 오늘 들어온 요청 리스트 갱신
        for request in new_requests(URL, auth_key):
            id = request['id']
            amount = request['amount']
            checkin = request['check_in_date']
            checkout = request['check_out_date']
            new = (amount, id, checkin, checkout, min(now + 14, checkin - 1))
            request_list.append(new)

        # 객실 배정 요청이 많은 순으로 정렬
        request_list.sort()
        request_list.reverse()

        # 각 요청마다 답변
        for request in request_list:
            id = request[1]
            amount = request[0]
            checkin = request[2]
            checkout = request[3]
            deadline = request[4]
            # 답변 기한이 지났다면 리스트에서 삭제
            if (now > deadline):
                request_list.remove(request)
            else:
                # 각 층을 확인하면서 해당 날짜에 amount가 가능한지 확인
                flag = False
                for floor in range(1, 4):
                    amount_tmp = 0
                    rooms_tmp = []
                    for num in range(1, 21):
                        room_number = (floor * 1000) + (num)
                        # 체크인부터 체크아웃 날짜 전까지 확인
                        for day in range(checkin, checkout):
                            # 해당 날짜에 예약이 되어있다면 다음 방부터 새로 확인
                            if day in book[room_number]:
                                amount_tmp = 0
                                rooms_tmp = []
                                break
                            # 해당 날짜에 예약이 되어있지않다면
                            if day == checkout - 1:
                                # 객실 추가
                                amount_tmp += 1
                                rooms_tmp.append(room_number)
                                if amount_tmp >= amount:
                                    flag = True
                                    break
                        if flag:
                            reply_list.append({ "id": id, "reply": "accepted"})
                            # (id, 예약 객실 배열)
                            reserved[checkin].append((id, rooms_tmp))
                            request_list.remove(request)
                            for room_number in rooms_tmp:
                                book[room_number] += [i for i in range(checkin, checkout)]
                            break
                    if flag:
                        break

        # 답변 보내기
        reply(URL, auth_key, reply_list)

        # 오늘자 체크인 진행
        room_assign = []
        for user in reserved[now]:
            room_assign.append({"id" : user[0], "room_number" : user[1][0]})
        print("today :", now)
        simulate(URL, auth_key, room_assign)

        # 하루 증가
        now += 1

    # 결과 확인
    score(URL, auth_key)
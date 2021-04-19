# play_time	adv_time	logs	result
# "02:03:55"	"00:14:15"	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	"01:30:59"
# "99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	"01:00:00"
# "50:00:00"	"50:00:00"	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	"00:00:00"

# 중복구간 중 중복구간 * 사람 이 가장 큰 구간찾기.
# 중복 구간 리스트 만들고. 
# 중복 구간 리스트 중 광고 시간과 비교하여 겹치는 부분에 대하여 사람수 만큼 곱하기. 
# time 클래스 사용?
# 초 단위로 계산하자. 시작초 -> 끝 초 사이에 중복이 가장 많은 구간.  git 
       

def make_s(time_list):
    time_s = 0
    for i in time_list:
        time_s = time_s*60 + i

    return time_s

def make_t(time_s):
    
    ss = str(time_s % 60)
    ss = '0'+ss if len(ss) < 2 else ss
    mm = str((time_s // 60) % 60)
    mm = '0'+mm if len(mm) < 2 else mm
    hh = str(time_s // 3600)
    hh = '0'+hh if len(hh) < 2 else hh
    
    # for i in range(3):
    #     tmp = time_s % 60

    return [hh,mm,ss]
def solution(play_time, adv_time, logs):
    answer = ''
    
    play_time_list = list(map(int,play_time.split(":")))
    adv_time_list = list(map(int,adv_time.split(":")))
    play_time_s = make_s(play_time_list)
    adv_time_s = make_s(adv_time_list)
    print("play : {}, adv : {}".format(play_time_s, adv_time_s))
    # print(make_t(play_time_s))

    logs_list = []
    for log in logs:
        tmp_list = []
        splitdash = list(map(str, log.split("-")))
        for dash in splitdash:
            tmp_list.append(list(map(int,dash.split(":"))))
        logs_list.append([make_s(tmp_list[0]), make_s(tmp_list[1])])

    
    logs_list.sort()
    print(logs_list)
    # 시간 작은것 부터 큰 순으로 정렬.

    # 중복 되는 구간 찾기.... 어떻게 할것인가. 
    # 겹치는 구간이 있는 애들만 선별.
    same_times = []
    max_time = -1
    
    for i in range(0,len(logs_list)-1):
        sum_time = 0
        start_point = 0
        for j in range(i+1, len(logs_list)):
            if j == i + 1:
            # 겹치지 않는 경우
                if logs_list[i][1] <= logs_list[j][0] : 
                    break
                else : 
                    short_pos = logs_list[i][1] if logs_list[i][1] < logs_list[j][1] else logs_list[j][1]
                    long_pos = logs_list[i][1] if logs_list[i][1] > logs_list[j][1] else logs_list[j][1]
                    # adv 타임이 전체 길이j[1] - i[0] 보다 큰경우 / j[1] 에 광고의 끝을 맞춤 
                    # 전체 길이보다는 작지만 i[1]-i[0] 보다는 큰경우
                    # i[1]-i[0] 보다는 작지만, i[1] - j[0] 보다는 큰경우
                    # i[1]j[0] 보다는 작은경우 

                    if adv_time_s > long_pos - logs_list[i][0]:
                        start_point = (long_pos - adv_time_s) if long_pos > adv_time_s else 0
                        sum_time = sum_time + (logs_list[i][1] - logs_list[i][0]) + (logs_list[j][1] - logs_list[j][0])
                        
                    elif adv_time_s > short_pos - logs_list[i][0]:
                        start_point = logs_list[i][0]
                        sum_time = sum_time + adv_time_s + (short_pos - logs_list[j][1])
                    
                    elif adv_time_s > short_pos - logs_list[j][0]:
                        start_point = short_pos - adv_time_s
                        sum_time = sum_time + adv_time_s + short_pos - logs_list[j][0]
                    
                    else : 
                        start_point = logs_list[j][0]
                        sum_time = sum_time + adv_time_s * 2
            else : 
                # 3번째 그 이상으로 겹치는 경우
                # start 포인트 부터 겹치는 부분 까지.     
                if start_point > logs_list[j][0]:
                    if start_point + adv_time_s > logs_list[j][1]:
                        sum_time = sum_time + logs_list[j][1] - start_point
                    else : 
                        sum_time = sum_time + adv_time_s
                    
                else :
                    # start point < logs_list[j][1]
                    if start_point + adv_time_s > logs_list[j][0]:
                        sum_time = sum_time + adv_time_s - (logs_list[j][0] - start_point)
                    else :
                        sum_time = sum_time + adv_time_s

        if max_time < sum_time:
            max_time = sum_time
            answer= start_point
    answer = make_t(answer)
    # else :
    #     answer = ["00","00","00"]
    answer = ":".join(answer)
    return answer

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
# "99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	"01:00:00"
# "50:00:00"	"50:00:00"	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	"00:00:00"
print(solution(play_time, adv_time, logs))
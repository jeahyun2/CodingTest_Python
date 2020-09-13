# ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# 해당사항 없으면 - 

# 먼저 언어	직군	경력	소울 푸드	점수 분류
# dict ? 배열. 
def solution(info, query):
    answer = []
    info_map = []
    for i in info:
        split_string = i.split(" ")
        info_map.append(split_string)
    # search 알고리즘.
    # [조건]은 개발언어 and 직군 and 경력 and 소울푸드 점수 형식의 문자열입니다.
    query_map = []
    
    for q in query:
        q = q.replace("and", "").replace("  "," ")
        split_string = q.split(" ")
        query_map.append(split_string)
    #query_map[0] = [java, backend, junior, pizza, 100]
    for q in range(len(query_map)):
        count = 0 
        for i in range(len(info_map)):
            # 돌면서 해당되는 답이면, count
            check = True
            if int(info_map[i][4]) < int(query_map[q][4]) :
                check = False
                continue
            for j in range(4):
                # if info_map[i][j] != query_map[q][j] or query_map[q][j] != '-':
                if query_map[q][j] == '-':
                    continue
                if info_map[i][j] != query_map[q][j]:
                    check = False
                    break
            
            if check == True : 
                count = count + 1
        answer.append(count)  
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
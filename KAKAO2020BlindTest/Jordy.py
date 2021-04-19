# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# n은 5 이상 100 이하인 자연수입니다.
# build_frame의 세로(행) 길이는 1 이상 1,000 이하입니다.
# build_frame의 가로(열) 길이는 4입니다.

# build_frame의 원소는 [x, y, a, b]형태입니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.

# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
# 바닥에 보를 설치 하는 경우는 없습니다.

# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.

# 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
# 최종 구조물의 상태는 아래 규칙에 맞춰 return 해주세요.

# return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
# return 하는 배열의 원소는 [x, y, a] 형식입니다.

# x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
# a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

# n	build_frame	result
# 5	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
# 5	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

import copy

# 각 함수는 x,y 와 현재 지어진 상태를 받음. 
# 각 상태를 보고 판단하여 지으는 함수 혹은 제거하는 기능을 수행.
def add_list(build_value, operators):
    # build operators 의 내용을 다 더하자. 
    tmp_value = copy.copy(build_value)
    for oper in operators:
        tmp_value[0] = tmp_value[0]+oper[0]
        tmp_value[1] = tmp_value[1]+oper[1]
    return tmp_value

def create(build, switch, current,n):
    if build[1] == 0:
        return True
    gi = [build[0], build[1], 0]
    bo = [build[0], build[1], 1]
    up = [0, 1]
    down = [0, -1]
    left = [-1, 0]
    right = [1, 0]
   
    if switch == 0 :
        # 기둥
        # 동 라인에 보들이 한개라도 존재하는가? 혹은 아래에 기둥이 있는가
        if add_list(bo,[left]) in current or bo in current or add_list(gi,[down]) in current :
            return True
    elif switch == 1 :
        # 보
        # 아래에 동 라인, 혹은 오른쪽 아래 기둥이 존재하면, 
        if add_list(gi,[down]) in current or add_list(gi,[down,right]) in current :
            return True
        # 왼쪽, 오륹쪽 모드 보가 존재하는가?
        elif add_list(bo,[left]) in current and add_list(bo,[right]) in current:
            return True

    return False
def remove(build,switch, current,n):
    if build+[switch] not in current:
        return False
    gi = [build[0], build[1], 0]
    bo = [build[0], build[1], 1]
    up = [0, 1]
    down = [0, -1]
    left = [-1, 0]
    right = [1, 0]
    
    # 기둥 
    if switch == 0:
        if (add_list(gi,[left]) in current and add_list(bo, [up,left]) in current) or (add_list(gi,[right]) in current and add_list(bo,[up])):
            # 왼쪽 기둥과 보 조합, 오른쪽 기둥과 보 조합 이면, 
            return True
        elif add_list(bo,[left,left,up]) in current and add_list(bo,[left,up]) in current and add_list(bo,[up]) in current and add_list(bo,[right,up]) in current:
            # 보 4개가 연결된 상황이면, 아래 지워도 됨.
            return True
        elif add_list(gi,[up]) in current and (add_list(bo,[up,left]) in bo or add_list(bo,[up]) in bo) :
            #위에 2가지 케이스로 위에 기둥 케이스는 모두 포함되는 것 같음.
            return True
    elif switch == 1:
        if add_list(gi,[down]) in current :
            if add_list(bo,[right]) not in current : 
                # 보 아래 기둥이 있고 동시에 우측 보는 없는 경우.
                return True
            elif add_list(bo,[right]) in current and (add_list(gi,[right,down]) in current or add_list(gi,[right, right, down]) in current):
                # 보 아래 기둥이 있고 우측 보가 존재하면서 동시에 우측보를 이어주는 기둥이 존재하는 경우
                return True
        elif add_list(gi,[right,down]) in current:
            if add_list(bo,[left]) not in current : 
                # 보 우측 아래 기둥이 있고 동시에 왼쪽 보는 없는 경우.
                return True
            elif add_list(bo,[left]) in current and (add_list(gi,[down]) in current or add_list(gi,[left, down]) in current):
                # 보 우측 아래 기둥이 있고 좌측 보가 존재하면서 동시에 좌측보를 이어주는 기둥들이 존재하는 경우
                return True
        elif add_list(gi,[down]) in current and add_list(right,[down]) in current:
            return True
    return False

def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        build = []
        build.extend(frame[0:2])
        build_type = frame[2]
        build_able = frame[3]
        if(frame[0]<0 or frame[1]<0 or frame[0]>n or frame[1]>n):
            continue
        if build_able == 0:
            if remove(build, build_type, answer,n) :
                answer.remove(frame[0:3])
        else :
            if create(build,build_type,answer,n):
                answer.append(frame[0:3])
    
    return sorted(answer)

n= 5 # 벽면크기. 
# x, y, a, b. x,y 지어지는 위치. a=0 기둥 1 보. b =0 제거 1 설치
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] #건설요청
# build_frame= [[0,0,0,0],[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
# build_frame = [[0,0,0,1],[0,1,0,1],[1,0,0,1],[2,0,0,1],[4,1,0,1],[5,4,0,1],[4,4,1,1]]
# build_frame = [
#     [0,0,0,1], [0,1,0,1],[0,1,1,1],[0,2,1,1],[3,0,0,1],[3,1,0,1],[3,2,0,1],[2,3,1,1],
#     [0,2,0,1],[0,3,0,1],[0,3,1,1],[2,0,0,1],[2,1,0,1],[1,2,1,1],[4,0,0,1],[4,1,0,1],[4,2,0,1],[4,3,0,1],[4,4,0,1],[0,4,1,1],[3,4,1,1],
#     [1,3,0,1],[1,4,1,1],[2,4,1,1],[1,3,0,0],[1,4,1,0],[2,4,1,0],[3,4,1,0]
# ]

build_frame = [
    [0,0,0,1], [0,1,0,1],[0,2,0,1],[0,3,0,1],[0,2,0,0],[0,1,0,0],[0,0,0,0],[0,3,1,1],[0,3,0,0], [2,2,0,1],[1,1,0,1],[1,1,1,1]
]

# x,y,a x,y 그리고 타입. 
# result =[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]] # 실제 건설
# result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
# result = [[0,0,0],[0,1,0],[1,0,0],[2,0,0]]
# result = [[0,0,0], [0,1,0],[0,1,1],[0,2,0],[0,2,1],[0,3,0],[0,3,1],[1,2,1],[2,0,0],[2,1,0]]
# result = [
#     [0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1], [0, 3, 0], [0, 3, 1], [0, 4, 1], [1, 2, 1], [1, 4, 1], 
#     [2, 0, 0], [2, 1, 0], [2, 3, 1], [2, 4, 1], [3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 4, 1], [4, 0, 0], [4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0]
# ]
result = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0],[0,3,1]]

answer = solution(n, build_frame)
print(answer)
assert  answer == result
print("합격")



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

def addList(a,b):
    if len(a) != len(b):
        return a
    tmp = [0 for _ in range(len(a))]
    for i in range(len(a)):
        tmp[i]=a[i]+b[i]
    return tmp


# 각 함수는 x,y 와 현재 지어진 상태를 받음. 
# 각 상태를 보고 판단하여 지으는 함수 혹은 제거하는 기능을 수행.
def create(build, switch, current):
    # current == [] 
    
    if build[1] == 0 and switch == 0 :
        # 바닥에 있으면 기둥은 무조건 건설. 
        return True
    else:
        # if ... in current : 
        tmp_lbo = [build[0]-1, build[1], 1]
        tmp_rbo = [build[0]+1, build[1], 1]
        tmp_lgi = [build[0], build[1]-1, 0]
        tmp_rgi = [build[0]+1, build[1]-1, 0]
# 4,2,1 
        if switch == 0 and (tmp_lbo in current or tmp_lgi in current) :
            # 만들려는게 기둥인 경우, tmp_bo 나 tmp_gi 가 존재하면 만들자.
            return True
        elif switch == 1 :
            # 만들려는게 보 인경우
            # 왼편이나 오른편에 기둥이 있으면 바로 보를 건설 가능.
            # 왼편에 보가 있으면 우편에 보나 기둥이 있어야함.(기둥은 이미 위에서 확인했으므로)
            if tmp_lgi in current or tmp_rgi in current :
                return True
            elif tmp_lbo in current and tmp_rbo in current:
                return True 
            # (tmp_lbo in current and (tmp_rbo in current or tmp_rgi in current):                
    return False
def remove(build,switch, current):
    # 기둥 / 위에 보가 없는 상태에서 기둥이 있으면 제거 불가.
    # 기둥 / 위에 연결된 보가 open 상태이면 기둥 제거 불가. 
    tmp_gi = [build[0], build[1], 0]
    tmp_bo = [build[0], build[1], 1]
    
    up = [0,1,0]
    down = [0,-1,0]
    left = [-1,0,0]
    right = [1,0,0]
    

    
    if switch == 0 :# 지우려는게 기둥인 경우 
        # 왼쪽 위에만 보가 존재하는 상황
        if addList(tmp_bo, up) not in current and addList(tmp_bo,addList(up, left)) in current and addList(tmp_gi, left) not in current : 
            # 우측 보가 없는 상태에서 왼쪽에 보에 기둥이 없는 경우. 
            return False
        elif addList(tmp_bo, addList(up,left)) in current and addList(tmp_bo,up) in current :
            # 왼쪽과 오른쪽에 보가 있는 경우. 
            if addList(tmp_gi, left) not in current and addList(tmp_bo, addList(up, addList(left, left))) not in current :
                # 왼쪽 기둥이 없는데 붙은 보가 없는 경우
                return False
            if addList(tmp_gi,right) not in current and addList(tmp_bo, addList(up, right)) not in current : 
                # 우측에 기둥이 없는데 우측으로 붙은 보가 없는 경우
                 return False 
        elif addList(tmp_bo, addList(up,left)) not in current and addList(tmp_bo, up) in current and addList(tmp_gi,right) not in current :
            # 우측에만 붙은 경우 
            return False
    else :
        # 보를 삭제하는 경우 
        # 현재 보 제외하고 보에 있는 기둥과 연결된 구조물이 없는 경우
        # 양 옆에 보가 존재할 때, 좌 혹은 우에 기둥이 존재하지 않는 경우
        # 보의 왼쪽에 연결된 기둥
        if tmp_gi in current and addList(tmp_bo,left) not in current and addList(tmp_gi,down) not in current:  
            return False
        elif addList(tmp_gi,right) in current and addList(tmp_gi, addList(right, down)) not in current and addList(tmp_bo, right) not in current:
            # 보의 오른쪽에 연결된 기둥
            return False
        elif addList(tmp_gi,down) in current and addList(tmp_bo,right) in current and addList(tmp_bo, addList(right,right)) not in current and addList(tmp_bo, addList(down, addList(right + right))) not in current:
            # 왼편에 기둥이 있는 상태에서, 오른쪽에 보가 연결된 경우 오른쪽과 그 아래 확인 필요
            return False
        elif addList(tmp_gi, addList(right,down)) in current and addList(tmp_bo,left) in current and addList(tmp_bo, addList(left, left)) not in current and addList(tmp_gi, addList(left, down)) not in current : 
            return False
        elif addList(tmp_gi,down) not in current and addList(tmp_gi, addList(right, down)) not in current :
            # 양쪽에 모두 기둥이 없는 경우
            if (addList(tmp_bo, left) in current and addList(tmp_gi, addList(left, down)) not in current) or (addList(tmp_bo,right) in current and addList(tmp_gi, addList(right, addList(right,down))) not in current):
                return False

    return True

def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        build = []
        build.extend(frame[0:2])
        build_type = frame[2]
        build_able = frame[3]
        if build_able == 0:
            if remove(build, build_type, answer) :
                answer.remove(frame[0:3])
        else :
            if create(build,build_type,answer):
                answer.append(frame[0:3])

    return answer

n= 5 # 벽면크기. 
# x, y, a, b. x,y 지어지는 위치. a=0 기둥 1 보. b =0 제거 1 설치
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] #건설요청
build_frame= [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
# x,y,a x,y 그리고 타입. 
# result =[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]] # 실제 건설
result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

print(solution(n, build_frame))
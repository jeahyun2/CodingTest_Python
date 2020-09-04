# 고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 
# 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 
# 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 
# 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 
# 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.


# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
# M은 항상 N 이하입니다.
# key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
# 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

# key 를 4번 회전하여 비어있는 곳으로 들어가면 True. 

def lotate(key):
    # key 를 90도 방향으로 돌리기.
    n = len(key)
    tmp_key = [ [ 0 for i in range(n)] for j in range(n) ]
    
    for i in range(n):
        for j in range(n):
            tmp_key[i][j] = key[n-1-j][i]
    return tmp_key

def is_array_fill_one(a,b,i,j,k,m):
# b array 의 모든값이 1 이여야 함. 
    # 범위 n-1:n**2-n
    # 범위 n-1 : 2n -1
    # lock = 0,0 - 2,2 / map = 2,2 - 4,4
    n = len(b)
    for i in range(n):
        for j in range(n):
            if a[n-1+i][n-1+j] + b[i][j] != 1 :
                return False
    return True

def solution(key,lock):
    
    # 4번 돌면서, key + lock 의 모든 배열의 합이 2를 넘지 않는 경우가 존재하면 True, 아니면 False.
    for i in range(4):
    # key 의 크기를 N 배 키워서 이 안에서 키를 움직였을 때 lock 이 충돌하지 않는 경우 찾기. 
        n=len(key)        
        
        # for i in range(len(tmp_map)):
        #     for j in range(len(tmp_map)):
        #         # tmp_map[i][j] = lock[i+n-1][j+n-1]
        
        # N = 3 일때 도는 횟수는 5번 n**2 - n - 1
        for i in range(n**2 -n - 1 ):
            for j in range(n**2 -n - 1 ):
                # tmp_map 의 특정 범위에 key 값을 더한다.  
                # 더해진 tmp_map 의 특정 범위와 lock 을 is_array_more_two 함수로 보내 확인한다. 
                tmp_map = [[0 for x in range(n**2-2)] for y in range(n**2-2)]
                # print(tmp_map)
                for k in range(n):
                    for m in range(n):
                        tmp_map[i+k][j+m] = key[k][m] #tmp_map[i+k][j+m] + key[k][m]
                
                if is_array_fill_one(tmp_map,lock,i,j,k,m):
                    print(tmp_map)
                    return True
        
        key = lotate(key)
    return False 

# 문제에서 이동 부분을 빼먹음. 이동에 대한 구현이 필요
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	

print(solution(key,lock))

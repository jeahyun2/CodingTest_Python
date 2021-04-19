
class Robot():
    legs = [] 
    route = []
    def __init__(self):
        # [행][열]
        self.legs.append([1,1])
        self.legs.append([1,2])

    def move_up(self):
        # 가능한지 확인된 상태
        self.legs[0][0] = self.legs[0][0] - 1
        self.legs[1][0] = self.legs[1][0] - 1
    def move_down(self):
        # 가능한지 확인된 상태
        self.legs[0][0] = self.legs[0][0] + 1
        self.legs[1][0] = self.legs[1][0] + 1

    def move_left(self):
        # 가능한지 확인된 상태
        self.legs[0][1] = self.legs[0][1] - 1
        self.legs[1][1] = self.legs[1][1] - 1
    def move_right(self):
        # 가능한지 확인된 상태
        self.legs[0][1] = self.legs[0][1] + 1
        self.legs[1][1] = self.legs[1][1] + 1    
    def rotate_90(self):
        self.legs[0][0] = self.legs[0][0] + 1
        self.legs[0][1] = self.legs[0][1] + 1
    def rotate_m90(self):
        self.legs[0][0] = self.legs[0][0] - 1
        self.legs[0][1] = self.legs[0][1] - 1
    def rotate_r(self):
        self.legs[1][0] = self.legs[1][0] + 1
        self.legs[1][1] = self.legs[1][1] - 1
    def rotate_rm90(self):
        self.legs[1][0] = self.legs[1][0] - 1
        self.legs[1][1] = self.legs[1][1] + 1
    
    def push(self, pos):
        self.route.append(pos)
    def pop(self):
        return self.route.pop(len(self.route)-1)
        
    def __str__(self):
        return "position : {}.{}".format(self.legs[0], self.legs[1])
    def curpos(self):
        return [self.legs]

def solution(board):
    answer = 0
    robot = Robot()
    n = len(board)
    # n+2 , n+2 사이즈를 갖는 새로운 보드 만들어서 대입. 
    new_board = [ [1 for _ in range(n+2)] for _ in range(n+2)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            new_board[i][j] = board[i-1][j-1]

    print(new_board)
    print(robot)
    # 1 마스킹 된 상태이므로, 시작점 1,1 종료지점 n,n
    while (robot.curpos()[0] != new_board[n][n] or robot.curpos()[1] != new_board[n][n]):



    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
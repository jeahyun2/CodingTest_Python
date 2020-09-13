def phase1(new_id):
    return new_id.lower()
def phase2(new_id):
    special_char = []
    special_char.extend("~!@#$%^&*()=+[{]}:?,<>")
    for char in special_char:
        new_id = new_id.replace(char, "")
    return new_id
def phase3(new_id):
    oldlen = len(new_id)
    new_id = new_id.replace("..",".")
    while(True):
        old_id = new_id
        new_id = new_id.replace("..",".")
        if old_id == new_id:
            break
    return new_id
def phase4(new_id):
    new_list = []
    if len(new_id) == 0:
        return ""
    new_list.extend(new_id)
    if len(new_list) == 1 and new_list[0] == '.' or len(new_list) == 0:
        new_id = phase1("")
    
    if len(new_list) > 1 and new_list[0] == '.':
        new_list.pop(0)
        new_id = "".join(new_list)
    
    if len(new_list) > 1 and new_list[-1] == ".":
        new_list.pop(len(new_list)-1)
        new_id = "".join(new_list)
    return new_id
def phase5(new_id):
    if len(new_id) == 0:
        new_id = "aaa" # 나중에 3개 매핑하므로
    return new_id
def phase6(new_id):
    if len(new_id) > 15:
        new_list = []
        new_list.extend(new_id)
        new_list = new_list[:15]
        new_id = "".join(new_list)
    return new_id
def phase7(new_id):
    if len(new_id) < 3:
        for i in range(len(new_id),3):
            new_id = new_id + new_id[len(new_id)-1]
    return new_id
    
def solution(new_id):
    answer = ''
    # 순서가 일부 변경 필요. 
    # 아무것도 없는 경우 제일 먼저. 
    
    while True:
        old_new_id = new_id
        new_id = phase1(new_id)
        new_id = phase2(new_id)
        new_id = phase3(new_id)
        new_id = phase4(new_id)
        new_id = phase5(new_id)
        new_id = phase6(new_id)
        new_id = phase7(new_id)
        if new_id == old_new_id:
            break
    
    return new_id

# -_.~!@#$%^&*()=+[{]}:?,<> 나타날 수 있는 특문. 
# 나타나도 되는 특문 . _ - 
# 알파벳 숫자. 
# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."	
new_id = "=.="	
# "123_.def"	
# "abcdefghijklmn.p"
print(solution(new_id))
# answer = "bat.y.abcdefghi"

# result = solution(new_id)
# assert result == answer


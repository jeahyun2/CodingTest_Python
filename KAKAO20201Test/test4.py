# n	s	a	b	fares	result
# 6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
# 7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
# 6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	18


def path(s,n, fare_grape):
    answer =0
    visited = [] # visied
    delta = [] # distance 
    queue = [] # queue

    delta = [ 10000 for _ in range(n+1) ] 

    delta[s] = 0
    queue.append(s)
    # 1번째 경우는 대입. 2번째 부터 비교
    cur = queue.pop(0)
    visited.append(cur)
    
    for key in fare_grape.keys():
        if key[0] == cur :
            if key[1] not in visited:
                queue.append(key[1])
                if delta[key[1]] > fare_grape[key] :
                    delta[key[1]] = fare_grape[key]
    
    
    while(queue):                
        # 2번째부터. 
        cur = queue.pop(0)
        if cur in visited:
            continue
        visited.append(cur)
        for key in fare_grape.keys():
            if key[0] == cur :
                if key[1] not in visited:
                    queue.append(key[1])                    
                    if delta[key[1]] > (delta[cur] + fare_grape[key]) :
                        delta[key[1]] = (delta[cur] + fare_grape[key])


    
    return delta
def solution(n, s, a, b, fares):
    answer = 0
    # print(n,s,a,b)
    # S-A, A-B
    # S-B, B-A
    # S-A, S-B 세가지 중 작은것 찾기.
    # dict 로 모든 길을 그래프로

    fare_grape = {}
    for fare in fares :
        f,l,value = list(map(int,fare))
        fare_grape[(f,l)] = value
        fare_grape[(l,f)] = value
    # print(fare_grape)
    delta = []
    delta = path(s,n,fare_grape)
    sa = delta[a]
    sb = delta[b]

    delta = path(a,n,fare_grape)
    ab = delta[b] 
    # print(sa, sb, ab)
    answer = 10000
    if sa + sb > sa + ab:
        answer = sa + ab
    else :
        answer = sa + sb
    if answer > sb + ab :
        answer = sb + ab
    return answer

# 7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
n=7
s=3
a=4
b=1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n,s,a,b,fares)) # result 82

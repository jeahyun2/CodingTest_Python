#!/usr/bin/env python3
# 데이터 처리 전문가가 되고 싶은 어피치는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 
# 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 
# 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
# 간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 
# 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 
# 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
# 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다. 
# 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 
# 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# 다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만, 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 
# 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

# s	result
# "aabbaccc"	7 / aabba3c 2a2baccc
# "ababcdcdababcdcd"	9 / 2ababcdcd / 숫자 문자열 숫자 문자열
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	17 x2ababcdcd

# 문자를 압축하여 가장 짧게 압축시킨 문자 수 리턴.
# 가장 많이 중복되는 길이 찾기.
# 1부터 n 까지 
# 

# s_list 에 전체 문자 넣고.
# 제일 작은 단위 찾기. 
# 맨 앞 문자 기준 같은 문자가 나오는 위치 찾기.
# 그 전까지 인덱스를 기준으로 찾은 문자 인덱스 와 비교 하여 같으면 시작 단위개수. 
# 시작 개수 부터 n/2 까지 비교. 

# 자를 수 있는 갯수가 정해짐. 
# 1개씩 자르면서 동시에 2개씩 자를수는 없음.
# 최대 자를 수 있는 크기 n/2
# 무조건 맨 앞 문자열 부터 반복이 들어가야함.

# 이해 안되는 케이스 
# "aabbaccc"	7 / aabba3c 2a2baccc 7이 나오기 위해서 2a2baccc 8, aabba3c 가 되어야 함. 
# "xababcdcdababcdcd"	17 x2ababcdcd 왜 x2ababcdcd 는 안되는거지?
# 
# 
import math
def solution(s):
    # len s = 3. 012. 
    # 3/2 1
    # # 제일 작은 반복 개수 찾기. abc abc abababababababababab 2단계가 제일 적은 수.
    # while m_index < len(s)//2 + 1:
    #     m_index = m_index + 1
    #     if 2*m_index >= len(s):
    #         break

    #     if s[s_index:m_index] == s[m_index:(2*m_index)] : 
    #         step = m_index
    #         break
    # s_index = 0
    tmp = []
    # 문제 다시. 갯수로 반복되는 알파벳을 압축하여 최소 압축 알파벳 개수 찾기.
    # 중복이 끝나고 남은 알파벳은 뒤에 붙이기. 

    min_count = len(s)
    # 남겨진 알파벳을 위한 코드..
    remian_index = 0

    for step in range(1, len(s)//2+1):
        # 시작 위치 1, step 의 초기 repeat word
        s_index = 1
        repeat_words = "".join(s[0:step])
        repeat_count = 1
        count = 0
        
        
        while (s_index + step) <= len(s):
            # 반복되는 단어인 경우. 반복 횟수 증가 단어 위치 증가
            if repeat_words == s[s_index:s_index+step]:
                repeat_count = repeat_count + 1
                s_index = s_index + step
            
            else : 
                # 10 보다 크면 1, 100보다 크면 2.. 
                # 조건에 맞지 않으면 현재까지 반복숫자+step(글자수) 를 count 하고, 
                # repeat count 초기화, s_index 는 1 증가.
                # repeat word 변경
                # repeat 2 이상인 경우 (반복이 1번이라도 나오는 경우)) 반복 알파벳 앞에 숫자 붙음. 10 이상인 경우, 2글자 이므로 log10 으로 계산.
                if repeat_count > 1 : 
                    count = count + int(math.log10(repeat_count))+1 + step
                else : 
                    # 앞에서 반복이 없었다면, 
                    count = count + 1
                repeat_count = 1
                repeat_words = "".join(s[s_index:s_index+step])
                s_index = s_index + 1
            if s_index + step > len(s):
                if repeat_count>1:
                    count = count + int(math.log10(repeat_count))+1+step
                else : 
                    count = count + 1
        if s_index < len(s)-1:
            #남은 글자가 존재하면, 그 글자수 count 에 추가.
            count = count + len(s) - s_index
        if min_count > count :
            min_count = count

    return min_count



            # if s[s_index:s_index+step] == s[s_index+step:s_index+2*step]:
            #     # 반복되는것 발견 시 repeat 리스트에 넣기. , repeat n 에는 반복 개수. 
            #     tmp = s[s_index:s_index + step]
            #     if tmp not in repeat_list:
            #         repeat_list.append(s[s_index:s_index + 2*step])
            #         repeat_count = 1
            #         repeat_n.append(repeat_count)
                    
            #     else :
                    
            #         index = repeat_list.index(tmp)
            #         repeat_n[index] = repeat_n[index]+1
            #     s_index = s_index + step*2
            # else :
            #     # 반복되는게 없는 경우 s_index 를 한개 증가.
            #     remian_index = s_index
            #     s_index = s_index+ 1 
                
# #        count = len("".join(repeat_list)) # 반복 구간의 alpa.

#         for i in range(len(repeat_n)):
#             count = count + len(str(repeat_n[i]))

#         if min_count > count :
#             min_count = count
    
#     return min_count

        # if len(tmp)==0 :
        #     tmp.append(s[s_index:step])

        # while 2*step < len(s):
        #     # 범위 넘어가지 않게. 
        #     # tmp 마지막 값이 반복 확인용. 
        #     # step 갯수로 반복되는 내용 찾기. 
        #     if tmp[len(tmp)-1] == s[step:2*step]:
        #         repeat_count = repeat_count + 1
        #         repeat_n.append(repeat_count)
        #     elif tmp[len(tmp)-1] != s[step:2*step]:


                
s = "aabbacccd"
print(solution(s))


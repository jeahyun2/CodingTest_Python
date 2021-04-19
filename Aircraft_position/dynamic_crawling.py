
# https://basicenglishspeaking.com/daily-english-conversation-topics/
# https://basicenglishspeaking.com/family/
# https://basicenglishspeaking.com/a-practical-skill/

# div class = sc_player_container1
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# 한 건의 대화에 대한 정보를 담는 클래스 입니다.
class Conversation(object):

    def __init__(self,q,a):
        self.q = q
        self.a = a

    def __str__(self):
        return "질문 : " + self.q + "\n답변 : " + self.a+"\n"


# 주제를 추출
def get_subject():
    subjects = []

    # 전체 주제 목록을 보여주는 페이지 경로 요청[reqeust] 객체 생성
    request = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = request.text
    bs = BeautifulSoup(html,'html.parser')

    divs1 = bs.find_all('div', {"class" : 'thrv_wrapper thrv_text_element'  })
    divs2 = bs.find_all('div', {"class" : 'thrv_wrapper thrv_text_element tve-froala fr-box'  })
    divs1.extend(divs2)

    for div in divs1:
        # 내부에 존재하는 a 태크를 추출합니다.
        links= div.find_all('a')
        # <a> 태크 내부의 텍스트를 리스트에 저장합니다.
        for link in links :
            subject = link.text
            subjects.append(subject)
    return subjects


subjects = get_subject()
print("총",len(subjects),"개의 주제를 찾았습니다")

conversations=[]


i=1
#모든 대화 주제 각각에 접근합니다.
for sub in subjects:
    print('(',i,'/',len(subjects),')',sub)
    # 대화스크립트를 보여주는 페이지를 요청[request] 객체를 생성합니다.
    req = requests.get('https://basicenglishspeaking.com/'+sub)
    html = req.text
    bs = BeautifulSoup(html,'html.parser')

    qnas = bs.find_all('div',{'class': 'sc_player_container1'})

    #qna 객체 대화내용에 접근합니다.
    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling
        else:
            a = qna.next_sibling
            c = Conversation(q,a)
            conversations.append(c)
    i = i +1
print("총",len(conversations),"개의 대화를 찾았습니다")

for c in conversations:
    print(str(c))

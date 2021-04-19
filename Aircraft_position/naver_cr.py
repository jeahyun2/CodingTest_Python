# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://nid.naver.com/nidlogin.login")
#
# # <input type="text" id="id" name="id" accesskey="L"
# # placeholder="아이디" class="int" maxlength="41" value="">
#
# time.sleep(1)
# driver.find_element_by_name('id').send_keys('jeahyun2')
# driver.find_element_by_name('pw').send_keys('insertinto')
#
# driver.find_element_by_xpath('//*[@id="log.login"]').click()
#
# driver.get('https://mail.naver.com')
# html = driver.page_source
# bs = BeautifulSoup(html, 'html')
#
# # 메일 제목을 하나하나 파싱
# title_list = bs.find_all('strong','mail_title')
#'
# for title in title_list:
#     print(title.text)
from urllib.request import urlopen
import bs4

index_cd = 'KPI200'
page_n = 1
naver_index = 'https://finance.naver.com/sise/sise_index.nhn?code=KPI200'+'$page='+str(page_n)

with urlopen(naver_index) as source:
    source = source.read()

source = bs4.BeautifulSoup(source, 'lxml')
print(source.prettify)

print(source.find_all('div', class_='provider_layer__txt'))



from1 = 'Xiamen (XMN)'
from2 = from1.split('(')
from3 = from2[1].split(')')
print(from3)



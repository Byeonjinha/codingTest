import os
from datetime import datetime
from selenium import webdriver
#가상 브라우저 실행

browser = webdriver.Chrome('./chromedriver.exe')

# 페이지 요청
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 수집하는 페이지 날짜 출력
span_viewday = browser.find_element_by_css_selector('div.cont-wrap > div > div.cmp-table-topinfo')
p = span_viewday.text
viewday = p.split('(')[0]
print('%s 수집시작' % viewday)

# 파일저장 디렉터리 생성
directory = "./Testweather/{:%Y-%m-%d}".format(datetime.now())
if not os.path.exists(directory):
    os.makedirs(directory)
#파싱하기
trs = browser.find_elements_by_css_selector('#weather_table > tbody > tr')
# 파일생성
fname = "Weather_{:%Y-%m-%d-%H-%M.csv}".format(datetime.now())
file = open(directory+'/'+fname,'w', encoding='utf-8')

for tr in range(0,len(trs)):
    p = ''.join(trs[tr].text.split(' '))
    file.write(p)
    file.write("\n")
file.close()
browser.quit()
print('데이터 수집 완료...')

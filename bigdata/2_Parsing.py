'''
날짜  : 2021-08-30
이름 : 변진하
내용 : 파이썬 HTML 페이지 파싱하기 실습
파싱(Parsing) 마크업 문서(반정형)에서 특정 태그의 데이터를 추출 처리하는 과정
'''

import requests as req
from bs4 import BeautifulSoup as bs

#페이지 요청
url = 'https://news.daum.net/ranking/popular'
html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text
# print(html)

#페이지 파싱
dom = bs(html, 'html.parser')
daum_titles= dom.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')
print(daum_titles)
for tit in range(5):
    print('%d위 : %s' % (tit+1,daum_titles[tit].text))

'''
pip install bs4

'''
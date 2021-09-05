"""
날짜 : 2021/08/31
이름 : 변진하
내용 : 파이썬 Selenium(가상브라우저) 패키지 실습
"""
from selenium import webdriver
#가상 브라우저 실행


browser = webdriver.Chrome('./chromedriver.exe')

'''
https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.107/ 설치
'''
#네이버이동
browser.get('https://naver.com')

#로그인 버튼 클릭
login_a = browser.find_element_by_css_selector('#account > a')
login_a.click()

input_id=browser.find_element_by_css_selector('#id')
input_pw=browser.find_element_by_css_selector('#pw')

input_id.send_keys('jinhaday')
input_pw.send_keys('nhy2468')

#로그인 버튼 클릭하기
button_login = browser.find_element_by_css_selector('#log\.login')
button_login.click()
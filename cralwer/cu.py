import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

# (참고1) https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/

URL = 'https://cu.bgfretail.com/event/plus.do?category=event'

driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=5)

driver.get(url=URL)

print(driver.title)
print(driver.current_url)


# 상품 더보기 버튼을 누르면 <ul>이 하나 더 생기는 구조.

#WebDriverWait(driver, 10).until(
#    EC.presence_of_all_elements_located((By.TAG_NAME, 'ul'))
#)
contents = driver.find_elements(By.ID, 'contents')
uls = contents.find_elements(By.TAG_NAME, 'ul')
last_ul = uls[-1]


li_elements = last_ul.find_elements(By.TAG_NAME, 'li')

print("이 밑으로 보일듯")
for li in li_elements :
	time.sleep(1)
	a_tag = li.find_element(By.TAG_NAME, 'a')
	#print(a_tag.get_attribute('href'))
	## a_tag 내의 모든 div 태그 찾기
	div_elements = a_tag.find_elements(By.TAG_NAME, 'div')

	# div 태그 개수 출력
	print(f"Number of div elements inside a_tag: {len(div_elements)}")
	prod_wrap = a_tag.find_elements(By.CLASS_NAME, 'prod_wrap')
	prod_text_div = prod_wrap.find_element(By.CLASS_NAME, 'prod_text')
	name_div = prod_text_div.find_element(By.CLASS_NAME, 'name')
	print(name_div.text)	

# 창 닫히지 않게 sleep(수집 종료되기 전까지 창이 꺼지지 않는지 확인하는 과정 필요)
time.sleep(10000)
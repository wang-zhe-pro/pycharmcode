from selenium import webdriver
import time
import  re
import re
broser=webdriver.Chrome()
url="https://www.guet.edu.cn/xwzx/gdxw/1.htm"
broser.get(url)
judge=broser.find_element_by_xpath('//*[@id="fanye160217"]').text
judgepage=re.findall("[\d]+",judge)
if(judgepage[1]==judgepage[2]):
    print("equ")
else:
    print("not")
broser.quit()
#加入selenium library 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#driver 的定義
driver = webdriver.Chrome('./chromedriver')

#該driver.get方法將定位在給定的URL的網頁。WebDriver將等到頁面完全加載（即，已觸發“ onload”事件），然後再將控制權返回給測試或腳本。
driver.get("https://www.google.com/?hl=zh-TW")

# 等待加載～
sleep(2)

# 使用css_selector查找網頁元素
print(driver.find_elements_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div"))

sleep(5)
#瀏覽器窗口關閉。您也可以調用quit方法而不是close。
driver.close()


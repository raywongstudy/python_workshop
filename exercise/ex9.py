
#加入selenium library 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

# chrome_options = webdriver.ChromeOptions()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

chrome_options.add_argument(f'user-agent={user_agent}')

executable_path = './chromedriver'# write your chromedriver path
driver = webdriver.Chrome(executable_path=executable_path , options=chrome_options)

#該driver.get方法將定位在給定的URL的網頁。WebDriver將等到頁面完全加載（即，已觸發“ onload”事件），然後再將控制權返回給測試或腳本。
driver.get("https://www.openrice.com/zh/macau/restaurants/district/%E6%BE%B3%E9%96%80")

# 等待加載～
sleep(1)

restaurant_list = []
list = driver.find_elements_by_css_selector(".title-name")

for i in list:
    restaurant_list.append(i.text)
    print(i.text)


#瀏覽器窗口關閉。您也可以調用quit方法而不是close。
driver.close()

print("chrome had close～～")


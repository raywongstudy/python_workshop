#加入selenium library 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#driver 的定義
driver = webdriver.Chrome('./chromedriver')

#該driver.get方法將定位在給定的URL的網頁。WebDriver將等到頁面完全加載（即，已觸發“ onload”事件），然後再將控制權返回給測試或腳本。
driver.get("https://www.youtube.com/")

# 等待加載～
sleep(1)

# 使用css_selector查找網頁元素 search box to input your data
driver.find_element_by_css_selector("#search[role=search]").send_keys("GEM鄧紫棋")

# 使用css_selector 按search 的按鍵 
driver.find_element_by_css_selector("#search-icon-legacy").click()

sleep(2)# 等待search結果～

# 使用css_selector 按search 的按 GEM 的channel
driver.find_element_by_css_selector(".style-scope.ytd-channel-renderer a").click()

sleep(1)# 等待search結果～

# 使用css_selector 按 影片的tab
driver.find_element_by_css_selector("#tabsContent > tp-yt-paper-tab:nth-child(4)").click()

sleep(1)# 等待 tap 結果～

# 使用css_selector 提取 影片的lists
video_lists = driver.find_elements_by_css_selector("#items > ytd-grid-video-renderer")

print("GEM最新音樂列表：")
print("----------------")
# 把影片的lists的文字print出來
for i in video_lists:
    print(i.find_element_by_css_selector("#video-title").text)

print("----------------")
# 把最新的影片打開
video_lists[0].click()

sleep(15)# 等待一下再關閉

#瀏覽器窗口關閉。您也可以調用quit方法而不是close。
driver.close()

print("chrome had close～～")


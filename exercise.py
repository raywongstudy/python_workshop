import time


name = input("what is your name:")
print("Hello "+name+" welcome you!")

sleep_time = input("How long you want to sleep:")


if(int(sleep_time) < 10):
	time.sleep(int(sleep_time))
else:
	print("the sleep time so long!")

print("please wake up!")

# 引入 requests 模組
import requests

# 使用 GET 方式下載普通網頁
r = requests.get('https://www.google.com.tw/')

if(r.status_code == 200):
	print(r.text)
else:
	print("you get some error!")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 

driver = webdriver.Chrome('/Users/raywong/Desktop/python_workshop/chromedriver')
driver.get("https://app.ssm.gov.mo/healthPHD/page/index.html")

def multiselect_set_selections(driver, element_css, labels):
    el = driver.find_element_by_css_selector(element_css)
    for option in el.find_elements_by_tag_name('option'):
        if option.text in labels:
            option.click()

driver.implicitly_wait(10)
driver.switch_to_frame("bar")

start_btn = driver.find_element_by_css_selector('.btn.btn-primary.btn-lg.bfg')
start_btn.click()

sleep(1)

start_btn = driver.find_element_by_css_selector('.checkbox > label')
start_btn.click()

start_btn = driver.find_element_by_css_selector('#btnAgree')
start_btn.click()

sleep(1)

name_input = driver.find_element_by_css_selector('[name="surname"]')
name_input.send_keys('RAY WONG')


multiselect_set_selections(driver,'[name=\'sex\']','男')

multiselect_set_selections(driver,'[name="dob_year"]','1999')

multiselect_set_selections(driver,'[name="dob_month"]','1')

multiselect_set_selections(driver,'[name="dob_day"]','1')

driver.find_element_by_css_selector("[name='idType']").click()
driver.find_element_by_css_selector("[name='tel_type']").click()

id_input = driver.find_element_by_css_selector("[name='idNum']")
id_input.send_keys('1234567(8)')
id_input = driver.find_element_by_css_selector("[name='tel_macau']")
id_input.send_keys('66123456')

driver.find_element_by_css_selector("[name='symptom'][value='99']").click()
driver.find_element_by_css_selector("[name='symptau'][value='N']").click()
driver.find_element_by_css_selector("[name='abefore_place']").click()

driver.find_element_by_css_selector("#btnSubmit").click()
sleep(.5)
driver.find_element_by_css_selector(".btn.btn-success.btn-block.bfs").click()
sleep(.5)


try:
	driver.find_element_by_css_selector("[name='agreement']").click()
	driver.find_element_by_css_selector("#btnGenDeclaration").click()
except:
	print('ok')


sleep(.5)

driver.find_element_by_css_selector("#btnReset").click()
sleep(.5)

try:
	driver.find_element_by_css_selector("[name='agreement']").click()
	driver.find_element_by_css_selector("#btnGenDeclaration").click()
except:
	print('ok')


sleep(100)

driver.close()
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(30)
win_id=driver.current_window_handle
print(win_id)
time.sleep(6)

driver.find_element_by_xpath("//span[text()='Login'] ").click()
mul_win_id=driver.window_handles
print(mul_win_id)
print(type(mul_win_id))
# print(mul_win_id[1])
driver.switch_to.window(mul_win_id[1])
driver.find_element_by_id("inputEmail").send_keys("test")

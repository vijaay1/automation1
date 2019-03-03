from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//input[@id='u_0_j']").send_keys("vijay")
driver.find_element_by_xpath("//input[@id='u_0_l']").send_keys("sharma")
# driver.find_element_by_xpath("//input[@id='u_0_s']").send_keys('7727066691')
# driver.find_element_by_xpath("//input[@name='reg_passwd__']").send_keys('qwerty1234567')
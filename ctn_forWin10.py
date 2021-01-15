from selenium import webdriver


data = []
for line in open("setting.txt", "r"):  # 设置文件对象并读取每一行文件
    data.append(line)
usr_name = data[0]
ps_word = data[1]
url = "http://detectportal.firefox.com/"


def test_url():
    import os
    return1 = os.system('ping 8.8.8.8 -n 3 -w 50')
    print(return1)  # ping通应该返回0
    if return1:
        return True  # 无法连外网就返回true
    else:
        return False  # 通的就返回false


while True:
    if test_url():
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(usr_name)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(ps_word)
        driver.find_element_by_id("mobilelogin_submit").click()
        driver.quit()

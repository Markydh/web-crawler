# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# # title = driver.title
# # driver.implicitly_wait(0.5)
# # text_box = driver.find_element(by=By.NAME, value="my-text")
# # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# # text_box.send_keys("Selenium")
# # submit_button.click()
# # message = driver.find_element(by=By.ID, value="message")
# # text = message.text
# #
# # driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建 ChromeOptions 对象
options = webdriver.ChromeOptions()

# # 禁用加载 JavaScript
# options.add_argument('--disable-javascript')

# # 禁用加载图片
# options.add_argument('--blink-settings=imagesEnabled=false')

# # 使用无头模式
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
url = 'https://www.bilibili.com/v/popular/rank/all'
localUrl = ' http://localhost:8080/ '
driver.get(url)

index = driver.find_elements(By.CLASS_NAME, "info")
for i in index:
    print(i.text)
    # 在获取的数据基础上再用语句选取包含在其中的元素
    print(i.find_element(By.TAG_NAME, "a").get_attribute('href'))


# 获取输入框 使用driver.find_element(By,name="")方法
# 向输入框传递数据 使用send_keys("value")
ele = driver.find_element(By.CLASS_NAME, "nav-search-keyword")
ele.send_keys("圣诞星")

# 按钮点击事件 click()函数
button = driver.find_element(By.CLASS_NAME, "nav-search-btn")
button.click()

# 打印网页信息



# print(driver.page_source)  # 打印网页的源码
# print(driver.get_cookies())  # 打印出网页的cookie
# print(driver.current_url)  # 打印出当前网页的url





import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# 记录开始时间
start_time = time.time()

option = webdriver.ChromeOptions()
# 禁用加载 JavaScript
option.add_argument('--disable-javascript')

# 禁用加载图片
option.add_argument('--blink-settings=imagesEnabled=false')

# 使用无头模式
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)

# 创建模板url
url_template = 'https://sh.fang.lianjia.com/loupan/pg{}/'

# 创建一个空的列表，用于存储所有的房产数据
all_house_data = []

for page in range(1, 101):
    # 动态改变url，分别获取不同的页面信息
    url = url_template.format(page)
    # 打开网页
    driver.get(url)
    # 获取房产元素列表
    house_elements = driver.find_elements(By.CSS_SELECTOR, '.resblock-list-wrapper li')

    # 处理房源信息
    for house_element in house_elements:
        # 小区名
        try:
            name = house_element.find_element(By.CSS_SELECTOR, '.resblock-name a').text
        except:
            name = None

        # 房屋类型
        try:
            house_type = house_element.find_element(By.CSS_SELECTOR, '.resblock-type').text
        except:
            house_type = None

        # 出售状态
        try:
            house_status = house_element.find_element(By.CSS_SELECTOR, '.sale-status').text
        except:
            house_status = None

        # 辖区
        try:
            district = house_element.find_element(By.CSS_SELECTOR, '.resblock-location span:nth-of-type(1)').text  # 辖区
        except:
            district = None

        # 城镇
        try:
            town = house_element.find_element(By.CSS_SELECTOR, '.resblock-location span:nth-of-type(2)').text
        except:
            town = None

        # 地址
        try:
            address = house_element.find_element(By.CSS_SELECTOR, '.resblock-location a').text
        except:
            address = None

        # 户型
        try:
            rooms = house_element.find_element(By.CSS_SELECTOR, '.resblock-room').text
        except:
            rooms = None

        # 面积
        try:
            area = house_element.find_element(By.CSS_SELECTOR, '.resblock-area').text
            area = area.split(" ")[1]  # 使用字符串切片提取空格后的部分，并去除空格
        except:
            area = None

        # 新房顾问
        try:
            Counselor = house_element.find_element(By.CSS_SELECTOR, '.ke-agent-sj-name').text
            Counselor = Counselor.split("：")[1].strip()  # 使用字符串切片提取冒号后的部分，并去除空格
        except:
            Counselor = None

        # 标签
        try:
            tag = house_element.find_element(By.CSS_SELECTOR, '.resblock-tag').text
        except:
            tag = None

        # 均价
        try:
            average_price = house_element.find_element(By.CSS_SELECTOR, '.number').text
        except:
            average_price = None

        # 总价
        try:
            total_price = house_element.find_element(By.CSS_SELECTOR, '.second').text
        except:
            total_price = None

        all_house_data.append({
            'name': name,
            'house_type': house_type,
            'house_status': house_status,
            'district': district,
            'town': town,
            'address': address,
            'rooms': rooms,
            'area': area,
            'Counselor': Counselor,
            'tag': tag,
            'average_price': average_price,
            'total_price': total_price
        })

    # 等待一段时间,以避免请求频率过高导致被封IP
    time.sleep(10)


# 记录开始时间
end_time = time.time()

# 从提取的数据创建一个DataFrame
df = pd.DataFrame(all_house_data)

# 将DataFrame保存为Excel文件
df.to_excel('all_house_shanghai_data.xlsx', index=False)

print(end_time-start_time)






import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

# 定义URL的模板
url_template = 'https://movie.douban.com/top250?start={}&filter='

# 创建一个空的列表，用于存储所有的电影数据
all_movie_data_list = []

# 循环遍历多个页面
for page in range(0, 250, 25):
    # 构建动态URL
    url = url_template.format(page)

    # 在浏览器中打开URL
    driver.get(url)

    # 获取电影列表元素
    movie_elements = driver.find_elements(By.CSS_SELECTOR, 'ol.grid_view li')

    # 处理电影信息
    for movie_element in movie_elements:
        title = movie_element.find_element(By.CSS_SELECTOR, '.title').text
        rating = movie_element.find_element(By.CSS_SELECTOR, '.rating_num').text
        year_country_genre = movie_element.find_element(By.CSS_SELECTOR, 'p').text

        # 检查是否存在 "inq" 类型的元素
        try:
            quote = movie_element.find_element(By.CSS_SELECTOR, '.inq').text
        except:
            quote = None

        all_movie_data_list.append({
            'Title': title,
            'Rating': rating,
            'Year_Country_Genre': year_country_genre,
            'Quote': quote
        })

    # 等待一段时间，以避免请求频率过高导致被封IP
    time.sleep(2)

# 关闭Selenium webdriver
driver.quit()

# 从提取的数据创建一个DataFrame
df = pd.DataFrame(all_movie_data_list)

# 将DataFrame保存为Excel文件
df.to_excel('all_movie_data.xlsx', index=False)

# 显示DataFrame
print(df)


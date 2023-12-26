import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("all_house_shanghai_data.xlsx")

data = data.replace('?', np.NaN)

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col, data[col].isna().sum()))

# 删除'total_price'为空的行
data = data.dropna(subset=['total_price'])

# 根据 house_type 分类统计数量
house_type_counts = data['house_type'].value_counts()

# 在每个柱上方显示数量
for i, value in enumerate(house_type_counts.values):
    plt.text(i, value, str(value), ha='center', va='bottom')

# 设置字体为中文
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# 画柱状图
plt.bar(house_type_counts.index, house_type_counts.values, color='skyblue')
plt.title('房屋类型分布')
plt.xlabel('房屋类型')
plt.ylabel('数量')
plt.show()





# 根据 house_type 分类统计数量
town = data['town'].value_counts()

# 在每个柱上方显示数量
for i, value in enumerate(town.values):
    plt.text(i, value, str(value), ha='center', va='bottom')

# 设置字体为中文
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# 画柱状图
plt.bar(town.index, town.values, color='skyblue')
plt.title('地区分布')
plt.xlabel('地区名')
plt.ylabel('数量')
plt.show()

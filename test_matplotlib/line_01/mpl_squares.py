import matplotlib.pyplot as plt

# 设置默认起点如果不设置的话默认起点为0
default_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 设置曲线并指定线的宽度
plt.plot(default_values, squares, linewidth=5)

# 设置图标标题， 并给坐标轴加上标签
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Vale", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 启动。
plt.show()
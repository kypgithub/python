import matplotlib.pyplot as plt

x_values= list(range(1, 1000))
y_values= [x**2 for x in x_values]
# c=y_values（表示使用颜色列表，渐变显示），cmap（表示使用什么颜色），edgecolors（轮廊阴影）， s（线条粗细）
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Numbers", fontsize=14)

# 设置刻度标记字体的大小（axis设置几个刻度{'x', 'y', 'both'}, which='major', labelsize=14字体大小）
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个做标值得取值范围（x/y）
plt.axis([0, 1100, 0, 1100000])
# 打开图形编辑器，并绘制图形
plt.show()
# 保存文件
# 第二个参数表数将图标多余得空白区域裁剪掉
# plt.savefig("squares_plot.png", bbox_inches='tight')
import matplotlib.pyplot as plt

from randow_spot_01.random_walk import RandomWalk

# 创建一个random_walk实例， 并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
point_number = list(range(rw.num_points))
# 设置绘图窗口尺寸
# figure函数接收一个元组单位为像素，用于指定图标得宽度、高度、分辨率、背景色, dpi指定屏幕大小
plt.figure(dpi=128, figsize=(10, 6))
# s表示spot得宽度
plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=2)
# plt.plot(rw.x_values, rw.y_values)
# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)
# 隐藏x/y坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()

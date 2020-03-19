import pygal

from die.die import Die

die = Die()

# 郑几次筛子将其结果放到列表中
results = []
for row_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides +1):
    count = results.count(value)
    frequencies.append(count)

# 可视化图
hist = pygal.Bar()
hist.title = "Results of rolling one D 1000 times"
hist.x_labels = [value for value in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file("die_visual.svg")
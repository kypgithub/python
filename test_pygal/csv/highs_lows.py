from matplotlib import pyplot as plt
from datetime import datetime
import csv

file_name = 'E:/python_projects/test_pygal/csv/sitka_weather_2014.csv'
with open(file_name, encoding='UTF-8') as file:
    reader = csv.reader(file)
    header_row = next(reader)

    # 获取标题
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# alpha表示透明度
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# 给高低两条曲线得连结部分着色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high and low temperatures - 2014", fontsize=10)
plt.xlabel('', fontsize=16)
# 绘制斜的日期标签
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=17)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

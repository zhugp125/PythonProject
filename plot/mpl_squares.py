import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
#添加数据源，并设置线宽
plt.plot(values, squares, linewidth=2)

#设置图表标题，并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
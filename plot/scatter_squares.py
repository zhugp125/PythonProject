import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#关联参数edgecolors=None去除轮廓线
#关联参数c='cyan'可以指定数据点的颜色，也可以用rgb颜色模式自定义颜色
#关联参数cmap=plt.cm.Blues表示颜色映射，颜色渐变
plt.scatter(x_values, y_values, cmap=plt.cm.Blues, edgecolors=None, c=None, s=40)

#设置图表标题，并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
#plt.savefig('square.png', bbox_inches='tight')
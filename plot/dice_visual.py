#/usr/bin/env python3

import pygal

from die import Die

# 创建两个六面的骰子
die_1 = Die()
die_2 = Die()

#掷几次骰子，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_reslut = die_1.num_sides + die_2.num_sides
for value in range(2, max_reslut + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 分析结果可视化
hist = pygal.Bar()

hist.title = 'Result of rolling two D6 dice 1000 times'
for value in range(2, die_1.num_sides + die_2.num_sides):
    hist.x_labels.append(str(value))
    
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
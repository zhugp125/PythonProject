# 一、字符串的连接和合并
# 1. 相加进行两个字符串的连接
str1 = 'Hello'
str2 = 'World'
new_str = str1 + ' ' + str2
print(new_str) #Hello World

# 2.join方法合并列表中的多个字符串
url = ['www', 'baidu', 'com']
print('.'.join(url)) #www.baidu.com

# 二、字符串的切片和相乘
# 1. 相乘
line = '*' * 30
print(line)

# 2. 切片
str1 = 'Hello World'
print(str1[0:5]) #Hello [0, 5)
print(str1[-3:]) #old   负数表示倒数
print(str1[:])   #复制

# 三、字符串的分割
# 1.普通的分割，用split
phone = '110-120-119'
print(phone.split('-'))

#复杂的分割
line = 'Hello World;  Python, I, like, It'
import re
# r前缀表示原始字符串，不使用转义
print(re.split(r'[;,s]\s*', line))

# 四、字符串的开头和结尾的处理
# 1. 开头处理
print('trace.h'.endswith('h'))

# 2. 结尾处理
print('trace.h'.startswith('trace'))

# 五、字符串的查找和匹配
# 1. 一般查找，返回查找的字串的位置，找不到返回-1
title = 'python can be easy to pick up and power full langage'
print(title.find('pick up'))

# 2. 复杂的匹配
mydate = '11/17/2017'
#import re
if re.match(r'\d+/\d+/\d+', mydate):
    print('ok, match')
else:
    print('no match')

# 六、字符串替换
# 1. 普通替换
title = 'python can be easy to pick up and power full langage'
print(title.replace('pick', 'upper'))

# 2. 复杂替换
#import re
students = 'Boy 103, gril 105'
print(re.sub(r'\d+', '100', students))

# 七、字符串去掉一些字符
line = '  Hello world  '
print(line.strip())
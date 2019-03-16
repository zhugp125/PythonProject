import os

path = '../file/'

# 判断文件是否存在
print(os.path.exists(path + 'test.txt'))

#重命名文件 重命名一个空文件会报错
if os.path.exists(path + 'test.txt'):
    os.rename(path + 'test.txt', path + 'test1.txt')

#删除文件 删除一个空文件会报错
if os.path.exists(path + 'test.txt'):
    os.remove(path + 'test.txt')

#文件路径的处理

path = '/user/python/data/info.txt'

#获得路径
print(os.path.dirname(path))

#获取文件名
print(os.path.basename(path))

#获取路径和文件名
print(os.path.split(path))

path = '../file/'

#创建并访问目录

#创建目录 创建一个已存在的目录会报错
if not os.path.exists(path + 'test1'):
    os.mkdir(path + 'test1')

#列出当前目录下的所有文件夹
print(os.listdir('.'))

#生成当前目录下的所有文件和目录
print(list(os.walk('.')))

#返回当前的目录
print(os.getcwd())

#删除一个空目录
if os.path.exists(path + 'test1'):
    os.rmdir(path + 'test1')

#判断是否为文件
print(os.path.isfile(path + 'test1.txt'))

#判断是否为目录
print(os.path.isdir(path))

#判断是否是为符号link 
# 在linux里面会有一些link文件
print(os.path.islink(path + 'test1.txt'))

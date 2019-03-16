# 一个面试题 range与xrange的区别 
# 这个面试题是基于python2.x的
# 因为python3.x已经没有xrange了，取而代之的是range

# 以下内容基于python2.x，在python2.7验证过

# range 
# 函数说明：range([start,]stop[,step]) 
# 根据输入的start和stop指定的范围，以及step指定的步长，生成一个序列 
# start默认为0 step默认为1

print(range(5))         #[0, 1, 2, 3, 4]
print(range(1, 5))      #[1, 2, 3, 4]
print(range(0, 5, 2))   #[0, 2, 4]

# xrange 
# 函数说明：用法与range完全一样，
# 区别在于range生成一个序列，xrange生成一个生成器

xrange(5)                    #xrange(5)
print(list(xrange(5)))       #[0, 1, 2, 3, 4]
xrange(1, 5)                 #xrange(1, 5)
print(list(xrange(1, 5)))    #[1, 2, 3, 4]
xrange(0, 5, 2)              #xrange(0, 5, 2)
print(list(xrange(0, 5, 2))) #[0, 2, 4]

#要生产很大的序列时，xrange性能要比range优越的多
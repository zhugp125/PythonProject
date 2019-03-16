#类型转换

#1 int()  把符合要求的数据转换为整形
# 如果是字符串，不能包含小数点和非数字字符
# 如果是浮点数，则把小数部分舍去
# 如果是整数，则原样输出

#正确的例子
print(int("123"))
print(int("0123"))
print(int("-123"))
print(int(123.45))  #123 舍入小数点数据
print(int(234))

#错误的例子
#print(int("aa"))
#print(int("23a"))
#print(int("2.3"))

#float函数将整数和字符串转换为浮点数

#正确的例子
print(float(123))
print(float(123.123))
print(float("124"))
print(float("124.124"))

#错误的例子
#print(float("aa"))
#print(float("23a"))

#str函数将数字转换为字符

#正确的例子
print(str(123))
print(str(123.124))
print(str("124"))
print(str("124.124"))
print(str("aaa"))
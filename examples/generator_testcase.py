# 用生成器来改写数据量较大的列表推导
# 推导式放到iterator中，就是（）
# list
a = [1, 2, 3, 4]
value = [x * 2 for x in a]
print(value)

# tuple
value = (x * 2 for x in a)
value_tuple = ((x, x * 2) for x in a)
print(value)
print(next(value))
print(next(value_tuple))

#

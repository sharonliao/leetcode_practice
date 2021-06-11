x_list = [1,2,3,4]
even_squares = [x**2 for x in x_list if x%2==0]
print(even_squares)


matrix = [[1,2,3],[10,11,12]]
# 就是把嵌套的for loop 摊平
# for row in matrix:
#     for x in row:
#         x+1

flat = [x+1 for row in matrix for x in row]
print(flat)




# 列表推导也支持多个if条件
a = [1,2,3,4]
b = [x for x in a if x>4 and x%2 ==0]

#the result of slicing a list is a whole new list
a = ['a','b','c','d','e','f']
b = a[3:]
print('Before:    ',b)
b[0] = 'AAAAA'
print('After:     ',b)
print('No change: ',a)
"""
Before:     ['d', 'e', 'f']
After:      ['AAAAA', 'e', 'f']
No change:  ['a', 'b', 'c', 'd', 'e', 'f']
"""



#when used in assignments, slices replace the specified range in the original list
print()
print('No change: ',a)
# 可以借用这种方式改变list的长度，在特定位置增删改查
a[3:4] = []
print('After:     ',a)
"""
No change:  ['a', 'b', 'c', 'd', 'e', 'f']
After:      ['a', 'b', 'c', 'e', 'f']
"""



b = a [:]
print('a:     ',a)
print('b:     ',b)
"""
a:      ['a', 'b', 'c', 'e', 'f']
b:      ['a', 'b', 'c', 'e', 'f']
"""

# stride 带步长的slice
b = a[::2]
print('a:     ',a)
print('b:     ',b)
"""
a:      ['a', 'b', 'c', 'e', 'f']
b:      ['a', 'c', 'f']
"""





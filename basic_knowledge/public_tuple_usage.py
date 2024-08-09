# 元组是不可变的，但要注意以下这种情况
'''
tuple = (1)     #指的是数字1
print(tuple)
tuple = (1,)    #指的是元组(1,) 
print(tuple)

# 下面两者指的是一个元组
tuple = (1,2,3,)
tuple = (1,2,3)
'''

# 元组没有独有的功能，只有一些公共的功能
# 求长度
'''
tuple = ("jaja",2,4,"3212",23,"[123]")
print(len(tuple))
'''


# 索引
'''
tuple = ("jaja",2,4,"3212",23,"[123]")
print(tuple[5])
'''


# 切片
'''
tuple = ("jaja",2,4,"3212",23,"[123]")
print(tuple[0:3])
'''


# for 循环
'''
tuple = ("jaja",2,4,"3212",23,"[123]")
for item in tuple:
    print(item)
'''


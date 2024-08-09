# 求长度len
'''
data_list = [123,456,789,135,246,357,987]
print(len(data_list))
'''

# 索引
'''
data_list = [123,456,789,135,246,357,987]

print(data_list[0],data_list[-1])  # 123 987

# 列表元素支持修改

data_list[0] = "renjie"
print(data_list)
'''

# 根据索引删除列表元素
'''
data_list = [123,456,789,135,246,357,987]
del data_list[1]
print(data_list)                # 456 has been deleted 
'''

# 切片
'''
data_list = [123,456,789,135,246,357,987]
print(data_list[0:4])
'''


# 支持for循环
'''
data_list = [123,456,789,135,246,357,987]
for item in data_list:
    print(item)
print("\n")
for i in range(len(data_list)):
    print(data_list[i])
'''
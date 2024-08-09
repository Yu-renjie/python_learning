# 求长度功能
'''
info = {"key1":123,
        "key2":"我是猪",
        123:True,
        False:(1,),
        (1,23,3):["renjie","brenjied"]}
print(len(info))  # 5
'''

#索引
'''
info = {"key1":123,
        "key2":"我是猪",
        123:True,
        False:(1,),
        (1,23,3):["renjie","brenjied"]}

print(info[(1,23,3)])           # 没有key的话会报错
print(info.get((1,23,3)))       # 推荐使用这种,因为可以添加非key输出的值,非key返回None
'''

# 增加 and 删除 and 修改
'''
info = {"key1":123,
        "key2":"我是猪",
        123:True,
        False:(1,),
        (1,23,3):["renjie","brenjied"]}

info["new"] = "a new guy"               # 添加到末尾了
print(info)

del info["new"]
print(info)                             # 删除了刚刚添加的new

info[False] = "hahaha"                  # 修改value为hahaha
print(info)
'''


#for 循环和 key value pair 联系使用

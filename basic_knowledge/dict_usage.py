 # 字典的获取值的方法
'''
info = {"key1":123,                         # key只能由可哈希的类型充当,int str tuple bool
        "key2":"我是猪",
        123:True,
        False:(1,),
        (1,23,3):["renjie","brenjied"]}
print(info.get(123))

print(info.get((1,23,3)))

print(info.get("dau"),"NOT FOUND")
'''


# print字典的key,value,pair
'''
info = {"key1":123,
        "key2":"我是猪",
        123:True,
        False:(1,),
        (1,23,3):["renjie","brenjied"]}

for item in info.keys():
    print(item)
print("\n")
for item in info.values():
    print(item)
print("\n")
for k,v in info.items():
    print(k,v)
'''

# 列表的定义
'''
list = [11, 22, 33]
list2 = ["num","name","code",11,22,33]
'''


# 列表的追加，在末尾追加数据
'''
user_list = []

while True:
    user = input("Please Enter your Username(Enter 1 to exit):")
    if user == "1":
        break
    else:
        user_list.append(user)

user_list = "The Userlist are:{}".format(','.join(user_list))
print(user_list)
'''


# 列表的插入，插入到指定位置
'''
user_list = []
while True:
    user = input("Please Enter Your Username(Enter 1 to exit):")
    if user == "1":
        break
    elif user.startswith("M"):
        user_list.insert(0,user)
    else:
        user_list.append(user)

user_list = "The Userlist are:{}".format(','.join(user_list))
print(user_list)
'''


# 列表元素的删除
'''
data_list = ["dgasj",123,"seha",723,"sdad","haha","haha"]
while "haha" in data_list:
    data_list.remove("haha")
print(data_list)
'''
'''
import random

user_list = ["dgasj",123,"seha",723,"sdad","haha","haha"]
lucky = random.choice(user_list)
lucky_msg = "Congratulations to {} win $500.".format(lucky)
print(lucky_msg)

user_list.remove(lucky)

lucky = random.choice(user_list)
lucky_msg = "Congratulations to {} win $1000.".format(lucky)
print(lucky_msg)
'''


# 列表的请空
'''
user_list = ["dgasj",123,"seha",723,"sdad","haha","haha"]
user_list.clear()
print(user_list)
'''

# 列表的排序
'''
list = [2, 34, 11, 55, 312, 78] 
list.sort()
print(list)
list.sort(reverse=True)
print(list)
'''


# 列表的翻转
'''
list = [2, 34, 11, 55, 312, 78] 
list.reverse()
print(list)
'''



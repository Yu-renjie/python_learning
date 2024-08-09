# 批量注释 "ctrl+？"

# TODO 注释的todo功能

# input输入的所有的东西全部是字符串

# 可变类型与不可变类型
# 不可变类型有：int str tuple bool
# 可变类型有：list dict 



# format 的用法
'''
adj = "tough"
major = "math"
text = "I'm a very {x1} guy,what's your {x2}".format(x2 = adj , x1 = major)
print(text)
text = "I'm a very {} guy,what's your {}".format(adj,major)
print(text)
text = "I'm a very {0} guy,what's your {1}".format(adj,major)
print(text)
'''

# 问题描述：用户输入用户名和密码，然后构造成tuple打包在list中，然后再按照用户输入，检查是否输入正确
'''
list = []
while True:
    user_name = input("Please Enter your Username(Enter The Q EXIT The Program):")
    if user_name.upper() == "Q":
        break
    psd = input("Please Enter your password:")
    msg = (user_name,psd)
    list.append(msg)
print(list)
'''

'''
list = [("brenjied","20031221"),("renjie","12345678"),("ethanyurenjie","5201314")]

user_name = input("Please Enter your Username:")
psd = input("Please Enter your password:")

is_Success = False

for item in list:
    if item[0] == user_name and item[1] == psd:
        is_Success = True
        break
    
if is_Success:
    print("Login Succed")
else:
    print("Mistake")
'''


# 问题描述： 输出一系列商品的名称价格序号
'''
goods = [
    {"title":"Computer","Price":"9000"},
    {"title":"Mouse","Price":"80"},
    {"title":"Keyboard","Price":"100"},
    {"title":"Bottle","Price":"90"},
    {"title":"Bag","Price":"9"},
]

for i in range(len(goods)):
    print(i+1,goods[i].get("title"),goods[i].get("Price"))


choice = int(input("Please select your goods:"))
print(goods[choice-1])
'''



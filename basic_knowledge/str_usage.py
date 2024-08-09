# 1. 判断以什么开头或者以什么结尾，返回值是 True or False

'''1.
str = "I am a good boy."
result = str.startswith("I")
print(result)
'''

'''2.
result ="I am a good boy".startswith("I")
print(result)
'''

'''3.
addr = input("Your Adress is:")
if addr.endswith("i"):
    print("city person")
else:
    print("country person")
'''



# 2. 判断字符串是否全部是数字

'''
print("欢迎使用xxx系统,请选择你要使用的功能:1.#####2.#####")
choice = input("输入你要选择的功能：")
if choice.isdecimal():
    msg = "你输入的信息是：{}".format(choice)
    print(msg)
else:
    print("输入有误")
'''


# 3. 大小写转化

'''
msg = "Root".upper()
msg = msg.upper()
new_msg = msg.lower()
print(msg)
print(new_msg)
'''


# 4. 去除空白或者换行符

'''
text = "    I am a Chinese   "
new_text = text.strip()
print(new_text)
new_text1 = text.rstrip()
new_text2 = text.lstrip()
print(new_text1)
print(new_text2)
'''


# 5. 替换功能

'''1.
data = "China  Shanghai  Move"
result = data.replace("China","America")
print(result)
result = result.replace('  ','')
print(result)
'''

'''2.
data = 'shanghai and beijing and suzhou'
key_list = ['shanghai','beijing']
for key in key_list:
    data = data.replace(key,"***")
print(data)
'''


# 7. 切割

'''1.
line ="Jie Ren,brenjied,1833907995"
data = line.split(',')

# data 是一个列表
print(data)                            
'''
'''''
2.
text = """Jie Ren,brenjied,1833907995,Num1
Jie Ren,brenjied,1833907995,Num2
Jie Ren,brenjied,1833907995,Num3
Jie Ren,brenjied,1833907995,Num4
Jie Ren,brenjied,1833907995,Num5
Jie Ren,brenjied,1833907995,Num6
Jie Ren,brenjied,1833907995,Num7
Jie Ren,brenjied,1833907995,Num8"""

data = text.split('\n')
print(data)
for key in data:
    key = key.split(',')
    print(key)
'''

# 8. 拼接

'''
list = ['renjie','male','1833907995','student']
new_list = ','.join(list)
print(new_list)
'''

# 9.字符串和字节,为了压缩储存

'''
data = "China Mobile"
result = data.encode("utf-8")
print(result)
data = result.decode("utf-8")
print(data)
'''

# Str Exercise
'''
import random
username = input("请输入你的用户名:").strip()
psd = input("密码:").strip()
code = random.randrange(1000,9999)
code = "验证码是：{}".format(code)
print(code)   
if username == "root" and psd == "qwe123":
    print("Success")
else:
    print("Mistake")
'''

import re

# 'renjie' 匹配文本中的renjie
text = "aduhasdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.findall('renjie',text)
print(data_list)
# ['renjie','renjie']

# '[renjie]' 匹配文本中的r或e或n。。。
text = "aduhasdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.findall('[renjie]',text)
print(data_list)
# ['j', 'r', 'e', 'n', 'j', 'i', 'e', 'e', 'n', 'j', 'i', 'j', 'n', 'i', 'j', 'i', 'r', 'e', 'n', 'j', 'i', 'e']

# 'ren[jie]' 匹配文本中的renj或reni或rene
text = "aduhasdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.findall('ren[jie]',text)
print(data_list)
# ['renj', 'renj']

# '[^renjie]' 匹配除r e n j i e 之外的字符
text = "aduhasdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.findall('[^renjie]',text)
print(data_list)
# ['a', 'd', 'u', 'h', 'a', 's', 'd', 'a', 'd', 'a', ' ', 'h', 'f', 'f', 'd', 'w', 'd', 'a', 's', 'k', 'd', 'a', 'o', ' ', 'q', 'f', ' ', 's', 'd', 'a', 's', 'd', 'u', ' ', 'b', 'a', 's', 'w', 'o', 's', 'd', 's', '我', '是', 's', 'd', 'a', 'b', 's', 'd', 'a', 's', 'k', 'm']


# 下面的都表达的是一个字符,多个字符数字无法表示
# 't[a-z]' 匹配ta tb tc 。。。't[0-9]'也可以
# 't.o'    . 匹配的是除了换行外的任意字符
# 't\wo'    \w匹配的是 字母and数字and汉字and下划线
# 't\do'    \d代表的是 匹配数字


# 多个字符的表达,以\d来举例
# 10个数字              \d\d\d\d\d\d\d\d\d\d
# 10个数字              \d{10}
# 至少10个数字           \d{10,}
# 重复10-15次            \d{10,15}
# 1个或者n个数字         \d+
# 0个或者1个数字         \d?
# 任意个数字             \d*

# re的贪婪匹配
text = "renjieshiyigeshuaigerenjie"
data_list = re.findall("r.+e",text)
print(data_list)
# ['renjieshiyigeshuaigerenjie']

# 怎样尽可能少的匹配
text = "renjieshiyigeshuaigerenjie"
data_list = re.findall("r.+?e",text)
print(data_list)
# ['renjie', 'renjie']



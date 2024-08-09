import re
# 除去findall的其他的一些函数


# match 从开头进行匹配
text = "aduhasdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.match('renjie',text)
print(data_list)
# None


text = "renjiesdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.match('renjie',text)
print(data_list)    # <re.Match object; span=(0, 6), match='renjie'>是一个对象

data_list = data_list.group()
print(data_list)
# renjie



# search  通篇找,但只找成功的第一个
text = "aduhasdada hffjrenjiedwendaskdjao qf sijdasnidu baswosdjsi我是sdabsdaskmrenjie"
data_list = re.search('renjie',text)
print(data_list)        # <re.Match object; span=(15, 21), match='renjie'>
if data_list:
    print(data_list.group())
# renjie


# 格式的校验
phone_num = input("Please enter your phone number:")
test = re.match("^1[3-9]\d{9}$",phone_num)
if test:
    print("Correct:",phone_num)
else:
    print("Incorrect.")
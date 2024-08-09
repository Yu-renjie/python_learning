import configparser

# 解析文件
parser = configparser.ConfigParser()
parser.read("my.ini",encoding="utf-8")


# 输出该文件的section部分，是一个列表
my_section = parser.sections()
print(my_section)
# ['General', 'Settings', 'Paths', 'Network']


# 输出section内部的item部分
my_item = parser.items("General")
print(my_item)
# [('appname', '示例应用'), ('version', '1.0.0'), ('author', '张三')]


# 解包
for k,v in my_item:
    print(k,v)
# appname 示例应用
# version 1.0.0
# author 张三


# 输出单独的一个section中的单独的一个value
my_value = parser.get('General','version')
print(my_value)
# 1.0.0


# ******************************************************************************************
# 上述操作可以去读取一个ini的文件
# 下面是一些其他的操作


# 删除
'''
parser.remove_option("General","version")
# 这一步只是在内存中的删除,需要进一步读取到文件中
parser.write(open('my.ini',encoding='utf-8',mode='w'))
'''
# 修改和添加
# parser.add_section("Group")
# parser.set('Group','datadir','hahaha')

# parser.write(open('my.ini',encoding='utf-8',mode='w'))



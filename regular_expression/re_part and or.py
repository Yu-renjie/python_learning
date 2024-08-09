# 实现在匹配时只匹配一部分，而非全体
import re
text  = "renjieshizaishiyigedashuaige,wofeichangdexihuanta,tashisheinejiushirenjieya"
data_list = re.findall("ren(jie\w)",text)
print(data_list)
# ['jies', 'jiey']

# 两个及以上的部分会形成元组
text  = "renjieshizaishiyigedashuaige,wofeichangdexihuanta,tashisheinejiushirenjieya"
data_list = re.findall("re(n(j)ie\w)",text)
print(data_list)
# [('njies', 'j'), ('njiey', 'j')]

# 也可以直接匹配整体
text  = "renjieshizaishiyigedashuaige,wofeichangdexihuanta,tashisheinejiushirenjieya"
data_list = re.findall("(re(n(j)ie\w))",text)
print(data_list)
# [('renjies', 'njies', 'j'), ('renjiey', 'njiey', 'j')]



# ************************************************************************************* #

# 当匹配时不止要匹配一部分，而是存在或的关系时
text  = "renjieshizaishiyigedashuaige,wofeichangdexihuanta,tashisheinejiushirenjieya"
data_list = re.findall("ren|jie",text)
print(data_list)
# ['ren', 'jie', 'ren', 'jie']


# 案例:匹配身份证号
text = "3477hdgfs152601200312213612fx5290ahdash237hf28t42g3178eg"
id_num = re.findall("\d{17}[\dX]",text)
print(id_num)
# ['152601200312213612']

# QQ号匹配:"[1-9]\d{4,}
# 手机号匹配:"1[3-9]\d{9}"
# 邮箱匹配:email_address = re.findall("\w+@\w+\.\w+",text,re.ASCII)



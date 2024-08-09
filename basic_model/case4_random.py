import random

# 生成四位的短信验证码
code = random.randint(1000,9999)            # 前后都取
print(code)


# 在列表中随机抽取数据
num_list = [2003,2004,2005,1221]
num = random.choice(num_list)               # 这个choice里可以放很多东西,包括函数
print(num)


# 随机打乱数据案例演示
# 构造一副扑克牌,随机打乱并且抽取

color_list = ['梅花','方片','红桃','黑桃']
num_list = range(1,14)

poke_list = []
for color in color_list:
    for num in num_list:
        poke = (color,num)
        poke_list.append(poke)

# 按照顺序排好的pokelist
# print(poke_list)

# shuffle poke
random.shuffle(poke_list)

# 随机抽取一张pokelist
my_poke = random.choice(poke_list)
print(my_poke)



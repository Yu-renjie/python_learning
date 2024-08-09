# 定义一个接受字符串的函数,在函数中统计有几个'a'字符并且返回其个数
'''
def counter(str):
    num = 0
    for char in str:
        if char =='a':
            num += 1
    return num

value = counter("sjdhausjdlkanaskdfuaalk")
print(value)
'''

# 生成器函数的作用:举例生成100000个连续的数字       标志是yield
'''
def creat_large_number(Max_size):
    num = 0
    while True:
        yield num
        if num == Max_size:
            return
        num += 1

large_num = creat_large_number(1000)
for item in large_num:
    print(item)
'''

# 装饰器函数  ******** 重点 *********
'''
def outer(func):
    def inner():
        print("before")
        func()
        print("later")
    return inner

@outer
def func():
    print("hahah")
    return 1
func()
# print(func())

'''


# 简单函数的lambda表达式
'''
def func(a,b):
    return a + b
value = func(2,4)
print(value)

func = lambda a,b : a + b
value = func(2,4)
print(value)
'''

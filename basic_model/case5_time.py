import time
import datetime

# 时间戳
until_now = time.time()
print(until_now)
# 1722841792.9639266            

# 程序执行计时
start = time.time()
data = 0
for i in range(1000000):
    data = i
print(data)
end = time.time()
print(end-start)


# 时间暂停
'''
while True:
    print(123)
    time.sleep(2)
# 每隔两秒执行一次
'''


# 当前时间，不同时区的时间
time1 = datetime.datetime.now()
print(time1)

timezone_7 = datetime.timezone(datetime.timedelta(hours = 7))
time2 = datetime.datetime.now(timezone_7)
print(time2)

zero_time_zone = datetime.datetime.utcnow()
print(zero_time_zone)

# 2024-08-05 16:49:59.727674
# 2024-08-05 15:49:59.727674+07:00
# 2024-08-05 08:49:59.727674


print("\n")
time_now = datetime.datetime.now()
print(time_now)

# 7天12小时22分钟46秒后的时间,也可以输出之前的时间
time_future = time_now + datetime.timedelta(days=7,hours=12,minutes=22,seconds=46)
print(time_future)
print("\n")
# 这时输出的时间是一个对象而不是字符串，可以方便的进行时间的加减



# 若要让用户输入时间，则是字符串的形式，这时就需要转换成字符串
# 对象类型 转换成 字符串 
time_obj = datetime.datetime.now()
time_str = time_obj.strftime("%m/%d/%Y %H:%M:%S")
print(time_str,type(time_str))
# 08/05/2024 17:18:11 <class 'str'>
print("\n")


# 字符串类型 转换成 对象类型 方便加减计算
time_str = "8/5/2024"
time_obj = datetime.datetime.strptime(time_str,"%m/%d/%Y")
print(time_obj)
# 2024-08-05 00:00:00
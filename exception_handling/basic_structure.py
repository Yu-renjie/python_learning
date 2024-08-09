import requests
import random


# 解决程序中不可预知的错误(程序无法考虑到的情况)
# 正常执行try里的,若报错则执行except里的

try:
    res = requests.get("https://www.bilibili.com/video/BV158411s7df?p=97&vd_source=62be967b1e98f12f53633a589ffbfa41")
    print(res.text)
except Exception as e:
    print("Error,Pls try on later.")




# 基本格式
'''
try:
    ...
    ...
except Exception as e:
    ...
    ...
'''
try:
    res = requests.gets("https://www.bilibili.com/video/BV158411s7df?p=97&vd_source=62be967b1e98f12f53633a589ffbfa41")
    print(res.text)
except Exception as e:
    print("Error,Pls try on later.",e)
# Error,Pls try on later. module 'requests' has no attribute 'gets'




# 特殊的finally:一般做资源的释放
# 注意:在函数中就算提前遇到return,也会最后一步执行finally

try:
    f = open("D:\\CS_learning\\vscode_project\\python_learning\\oo_program\\reflection.py",mode='r',encoding="utf-8")
    data = f.read()
    num = int(data)

except Exception as e:
    print("Error",e)

finally:
    f.close()
# Error invalid literal for int() with base 10: '# getattr(object, member)\n# setattr(object, member, value)\n\'\'\'\nclass Base:\n\n    def __init__(self):\n        self.x1 = "NYC"\n        self.x2 = "LA"\n\n\ndef main():\n    obj = Base()\n    pr



# 主动触发异常,在统一一个地方报错
def send_emile():
    num = random.randint(0,1)
    if num == 1:
        return True
    else:
        return False
    
try:
    res = send_emile()
    if not res:
        raise Exception("Failure")
    print("Success")

except Exception as e:
    print("Error",e)
# Error Failure
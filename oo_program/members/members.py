# 目前接触的成员有三种
# 一是方法 二是变量(对象定义的) 三是属性

'''
# 先看变量:分为实例变量和类变量
# 实例变量属于对象,类变量属于类
# 当每个对象中都有同样的值,为了防止内存开销过大,使用类变量,只保存一份即可
class Base:
    Country = "China"

obj = Base()
print(Base.Country)
# China
setattr(Base, "Country", "Amercia")
data = getattr(obj,"Country")
print(data,Base.Country)
# Amercia Amercia
'''

# ************************************************************************************ #

# 方法分为三类:绑定方法,静态方法,类方法

# 绑定方法
# 定义时:至少有一个self参数,哪个对象调用这个方法,self就是哪个对象
# 调用时: 对象.方法名称


# 静态方法:当方法中不会用到任何对象中封装的值时,可以使用静态方法
# 定义时:可以有任意个参数,但python内部不会帮它传递参数,使用时在前面加 @staticmethod
# 调用时:类名.方法名称  or  对象名.方法名称 


# 类方法:当前方法不需要对象,而是需要当前的类,就需要使用cls
# 定义时:至少有一个cls参数,cls是python内部自动传递,cls的值等于当前的类名
# 调用时:类名.方法名称  or  对象名.方法名称
'''
class Base:
    def __init__(self,n):
        self.x1 = n

    @staticmethod
    def show():
        print("This is a staticmethod.")        

    @classmethod
    def get_info(cls):
        pass

obj = Base(520)
Base.show()
Base.get_info()
'''
# ************************************************************************************ #

# 属性 ——> property

class Base:

    def send(self):
        return 123
    
obj = Base()

# 常规使用,但是由于并没有用到关于self的内容,故可以将send这个方法变成一个属性
data = obj.send()
print(data)


# 以下为属性的使用方法1
class Base:

    @property
    def send(self):
        return 123
    
obj = Base()

data = obj.send # 不再需要加括号了
print(data)

# 以下是属性的使用方法2
class Base:

    def send(self):
        return 123
    SEND = property(send)
    
obj = Base()

data = obj.SEND # 也不再需要加括号了
print(data)

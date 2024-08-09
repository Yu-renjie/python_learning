# 一些特殊的成员指的是一些特殊方法来定义的方法
# 如__init__等


# __init__初始化方法
from typing import Any


class Foo:
    def __init__(self,name) :
        self.name = name


obj = Foo("renjie")
print(obj.name)
# renjie


# __new__构造方法
# 创建一个新对象需要两步,首先创造一个新对象,其次为这个新对象赋值
# 原理是:每创建一个新类时,这个类的父类都是Object,但不用写出来,是python里默认的
# 而在Object类里,会自动执行__new__方法,即创建一个空对象

class Foo:
    def __init__(self,name) :
        print(1)
        self.name = name

    def __new__(cls, *args,**kwargs) :  
        print(2)
        empty_object = object.__new__(cls)
        return empty_object

obj = Foo("renjie") 
# 2
# 1


# 一般来说,类名()是给对象的值初始化
# 而对象()则调用类里面的__call__方法
class Foo:
    def __init__(self,name) -> None:
        self.name = name

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__")

obj = Foo("renjie")
obj()
# __call__


# __str__ 将对象以字符串输出
class Foo:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return "{}--{}".format(self.name,self.age)
    

obj = Foo("renjie",22)
print(obj)
# <__main__.Foo object at 0x000001A9CAC6F460>
# renjie--22


# __dict__获取对象的全部成员,并以字典的形式输出
class Foo:
    def __init__(self,name,age) :
        self.name = name
        self.age = age


obj = Foo("renjie",22)
print(obj.__dict__)
# {'name': 'renjie', 'age': 22}




# __getitem__  and  __stitem__  and  __delitem__
# obj[]
class Foo:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def __getitem__(self,item):
        pass
    def __setitem__(self,key,value):
        pass
    def __delitem__(self,item):
        pass

obj = Foo("renjie",22)
obj["sdada"]
obj["hadu"] = 123
del obj["sdjai"]




# __add__将两个对象相加
class Foo:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def __add__(self, other):
        return self.age + other.age

obj1 = Foo("renjie",22)
obj2 = Foo("baidi",22)

age = obj1 + obj2 # obj1.__add__(obj2)   obj1代表self obj2代表other 
print(age)
# 44
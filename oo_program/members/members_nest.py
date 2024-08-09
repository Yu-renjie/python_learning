# 对象间的相互嵌套
'''
class Students:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def info(self):
        print(self.name,self.age)

class Classes:
    def __init__(self,title) :
        self.title = title
        self.stu_list = []

    def add(self,stu):
        self.stu_list.append(stu)

    

class1 = Classes("1904")

stu1 = Students("renjie",20)
stu2 = Students("baidi",20)
stu3 = Students("zhangsan",22)

class1.add(stu1)
class1.add(stu2)
class1.add(stu3)

print(class1.title)
# 1904
print(class1.stu_list)
# [<__main__.Students object at 0x000001EDD305F430>, <__main__.Students object at 0x000001EDD305F790>, <__main__.Students object at 0x000001EDD305F7F0>]
class1.stu_list[0].info()
# renjie 20
print(class1.stu_list[1].name)
# baidi
'''

# 对象之间的链表关系
'''
class User:
    def __init__(self, name, next) :
        self.name = name
        self.next = next


zs = User("zhangsan",None)
bd = User("baidi",zs)     
rj = User("renjie",bd)


print(rj.next.name)
# baidi
'''
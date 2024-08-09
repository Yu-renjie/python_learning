# 要明确self到底是谁
# object是由哪个class定义的,那么优先去那里找对应的方法,若未找到,则去对应的父类找

'''
class Father:

    def f1(self):
        print("run f1")

    
class Son(Father):

    def f2(self):
        print("run f2")


def main():
    obj = Son()
    obj.f1()
    obj.f2()
# run f1
# run f2

if __name__ == "__main__":
    main()
'''

# ****************************************************************************** # 
'''
class Base:

    def f1(self):
        print("Base.f1")

class Son(Base):

    def f2(self):
        print("Son.f2")


class Grandson(Son):

    def f3(self):
        print("Grandson.f3")


def main():
    obj = Grandson()
    obj.f1()
    obj.f2()
    obj.f3()
# Base.f1
# Son.f2
# Grandson.f3

if __name__ == "__main__":
    main()
'''
# ****************************************************************************** # 
'''
class Base:

    def f1(self):
        print("Base.f1")

class Son(Base):
        
    def f2(self):
        print("Son.f2")


def main():
    obj = Son()
    obj.f1()
    obj.f2()
# Base.f1
# Son.f2


if __name__ =="__main__":
    main()
'''

# ****************************************************************************** # 
'''
class Base:

    def f1(self):
        print("Base.f1")

class Son(Base):

    def f1(self):
        print("Son.f1")

    def f2(self):
        print("Son.f2")
        self.f1()


def main():
    obj = Son()
    obj.f1()
    obj.f2()
# Son.f1
# Son.f2
# Son.f1

if __name__ =="__main__":
    main()
'''
# ****************************************************************************** # 
'''
class Base:

    def f1(self):
        print("Base.f1")

    def f2(self):
            print("Base.f2")
            self.f1()


class Son(Base):

    def f1(self):
        print("Son.f1")


def main():
    obj = Son()
    obj.f1()
    obj.f2()
# Son.f1
# Base.f2
# Son.f1

if __name__ =="__main__":
    main()
'''
# ****************************************************************************** # 
'''
class Base:

    def f1(self):
        print("Base.f1")


class Son:

    def f2(self):
        print("Son.f2")


# 多个子类时，从左往右依次找到其父类
class GrandSon(Son, Base):
    pass


def main():
    obj = GrandSon()
    obj.f2()
    obj.f1()
# Son.f2
# Base.f1

if __name__ == "__main__":
    main()
'''
# *************************************************************************** #
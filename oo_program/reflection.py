# getattr(object, member)
# setattr(object, member, value)
'''
class Base:

    def __init__(self):
        self.x1 = "NYC"
        self.x2 = "LA"


def main():
    obj = Base()
    print(obj.x1,obj.x2)
# NYC LA

if __name__  == "__main__":
    main()
'''
'''
class Base:
    pass

def main():
    obj = Base()
    obj.x1 = "NYC"
    obj.x2 = "LA"
    print(obj.x1,obj.x2)
# NYC LA


if __name__  == "__main__":
    main()
'''
'''
class Base:
    pass


def main():

    obj = Base()
    # obj.x1 = "NYC"
    setattr(obj,"x1","NYC")     
    setattr(obj,"x2","LA")

    data1 = getattr(obj,"x1")
    data2 = getattr(obj,"x2")

    print(data1, data2)
# NYC LA



if __name__  == "__main__":
    main()
'''

# 输出对象中的全体成员
class Base:

    def __init__(self):
        self.x1 = "NYC"
        self.x2 = "LA"


def main():
    obj = Base()
    obj.x3 = "HK"
    print(obj.__dict__)
# {'x1': 'NYC', 'x2': 'LA', 'x3': 'HK'}


if __name__  == "__main__":
    main()

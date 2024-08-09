# object: 根据类创建出来的一块区域,可以储存值,对象可以找到类中的方法并执行
# __init__:类中的一个特殊方法,此方法在 类名() 自动的执行,一般用于的给对象中的值进行初始化
# self 本身就是一个参数,不需要人为的传递值,python内部会将对象传递给它
'''
class UserInfo: 
    def __init__(self,user,psd):
        self.name = user
        self.password = psd

def main():
    user_list = []
    while True:
        
        user = input("Enter your name:")
        if user.upper() == 'Q':
            break
        psd = input("Enter your password:")
        
        group = UserInfo(user,psd)
        user_list.append(group)
    # print(user_list)        
    for ele in user_list:
        print(ele.name,ele.password)
                         
if __name__ == "__main__":
    main()
'''

class Police:
    def __init__(self,name):
        self.name = name        
        self.score = 100
    def help(self):
        self.score += 50

        
class Bad:
    def __init__(self,name): 
        self.name = name
        self.level = 100
    def zero(self):
        self.level += 25

    def arrest(self):
        self.level -= 50

def main():
    renjie = Police("任杰")
    renjie.help()

    apple = Bad("白迪")
    apple.zero()
    apple.zero()
    apple.arrest()

    print(renjie.name,renjie.score)
    print(apple.name,apple.level)
    
if __name__ == "__main__":
    main()
# 任杰 150
# 白迪 100

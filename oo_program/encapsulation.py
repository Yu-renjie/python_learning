# 把一类功能封装在一个object中
# 不同的class实现不同的功能

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

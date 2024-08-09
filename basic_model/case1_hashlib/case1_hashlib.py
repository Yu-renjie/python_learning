# hashlib   可以对数据进行加密的一个包  such as:md5
import hashlib


def encrypt(data_string):
    obj = hashlib.md5()
    obj.update(data_string.encode( "utf-8"))
    crypto_data = obj.hexdigest()
    return crypto_data


def save_to_file(msg):
    # 打开文件  mode a 指的是追加，没有的话会创建文件
    file = open("D:\\CS_learning\\vscode_project\\python_learning\\model\\case1.txt",mode='a',encoding="utf-8")
    # 写入文件
    file.write(msg)
    # 关闭文件
    file.close()


def read_file():
    # 打开文件 mode r 指的是只读
    file = open("D:\\CS_learning\\vscode_project\\python_learning\\model\\case1.txt",mode='r',encoding="utf-8")
    # 输出成一个字符串
    data_list = file.read()
    file.close()
    return data_list

# 解包
def unit_package(data_list):
    data_list = data_list.strip().split("\n")
    for item in data_list:
        username,password = item.split("|")
        print(username,password)


def main():


    # 用户输入用户名、密码
    user = input("Plesase Enter your Username:")
    pwd = input("Pleease Enter your Password:")

    # 对密码加密
    crypto_pwd = encrypt(pwd)

    # 对输入规范化
    line = "{}\t|{}\n".format(user,crypto_pwd)

    # 打开文件、写入内容、关闭文件
    save_to_file(line)

    # 打开文件、读取内容、关闭文件
    data_list = read_file()

    # 对读取到的内容解包并且输出到屏幕上
    unit_package(data_list)



   
if __name__ == "__main__":
    main()




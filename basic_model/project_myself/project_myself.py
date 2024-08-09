# request : 用户输入手机号,然后发送四位验证码,用户输入验证码,验证是否一致,一致的话将这些信息全部的写入文件
import random
import datetime

# 输入的一系列信息
def format_msg():
    while True:
        phone_num = input("Please Enter Your Phone number:").strip()
        if len(phone_num) == 11:

            code = random.randint(1000,9999)
            print("Your code is:",code)
            code_user = input("Please enter your code:")
            if code == int(code_user):
                time_obj = datetime.datetime.now()
                time_str = time_obj.strftime("%m/%d/%Y %H:%M:%S")
                msg = "{}\t{}\t{}\n".format(phone_num,code,time_str)
                return msg
            else:
                print("Incorrect code,please enter again.")
                continue
        else:
                print("Incorrect phone number,please enter again.")
                continue



# 创建文件,并将生成的list写入
def save_to_file(list):
    file = open("D:\\CS_learning\\vscode_project\\python_learning\\basic_model\\project_myself\\msg.txt",mode = 'a',encoding="utf-8")
    file.write(list)
    file.close()


def main():
    

    msg = format_msg()
    save_to_file(msg)



if __name__ == "__main__":
    main()




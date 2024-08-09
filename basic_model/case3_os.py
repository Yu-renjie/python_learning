'''
import os


# 获取文件的绝对路径
path = os.path.abspath('case1.txt')     
print(path)                 # D:\CS_learning\vscode_project\case1.txt

current_path = os.path.abspath(__file__)
print(current_path)         # d:\CS_learning\vscode_project\python_learning\model\case3_os.py

next_path = os.path.abspath('case2_json.py')
print(next_path)            # D:\CS_learning\vscode_project\case2_json.py



# 路径的拼接,不管路径是否存在,因为mac与win的文件连接不同
file_path = os.path.join("case1_hashlib","case1.txt")
print(file_path)                    # case1_hashlib\case1.txt



# 判断路径是否存在
whether = os.path.exists(file_path)
print(whether)


# 创建文件夹

folder_path = os.path.join("file1","file2","file3")
os.makedirs(folder_path)

# 查看目录下的文件  只能找一级
ab_path = os.listdir("D:\\CS_learning\\vscode_project\\python_learning")
print(ab_path)                                              
# ['.venv', 'basic_knowledge', 'basic_model', 'file1']

# 可以查看所有的文件夹的内部。。
all_path = os.walk("D:\\CS_learning\\vscode_project\\python_learning")         
# all_path 是一个对象，需要对其进行循环

for a,b,c in all_path:
    # a  D:\CS_learning\vscode_project\python_learning          进入该目录
    # b  ['.venv', 'basic_knowledge', 'basic_model', 'file1']   该文件夹的所有文件夹
    # c  []                                                     该文件夹下的所有文件

    print(a,b,c)
    break                                                      
# 如果不break的话自动进入下一个文件夹,再次按照上述顺序输出一遍


    
    
# 案例:输出目录下所有的以.txt结尾的文件

all_path = os.walk("D:\\CS_learning\\vscode_project\\python_learning") 
for dir, folder, file_list in all_path:
    for name in file_list:

        ext = name.split(".")[-1]

        if ext == "txt":
            print(name)

# top_level.txt
# entry_points.txt
# top_level.txt
# vendor.txt
# entry_points.txt
# LICENSE.txt
# top_level.txt
# top_level.txt
# entry_points.txt
# top_level.txt
# LICENSE.txt
# case1.txt
'''        
# oop与configparser包的结合案例
import configparser

class Settings:

    def __init__(self):
        self.language = str
        self.theme = str
        self.autosaveinterval = int

def main():
    settings_object = Settings()
    # 解析文件
    parser = configparser.ConfigParser()
    parser.read("settings.ini",encoding="utf-8")

    for field, data_type in settings_object.__dict__.items():
        '''print(field,data_type)'''

        # language <class 'str'>
        # theme <class 'str'>   
        # autosaveinterval <class 'int'>

        data_string = parser.get('Settings', field)
        real_data = data_type(data_string)

        '''print(field,real_data)'''
        # language zh-CN
        # theme Dark
        # autosaveinterval 10
        
        setattr(settings_object, field, real_data)

    print(settings_object.language,settings_object.theme,settings_object.autosaveinterval)     
    # zh-CN Dark 10



if __name__ =="__main__":
    main()
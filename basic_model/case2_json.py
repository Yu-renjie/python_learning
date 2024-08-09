# json格式就是一系列字符串，可以沟通不同的语言

import json

# json 反序列化     json字符串转化为python代码
data_list = '''{
    "globalObjects": {},
    "timeline": {
        "id": "Fl7jfjmaYAAAAAABiJONchMoIV0",
        "instructions": [
            {
                "addEntries": {
                    "entries": [
                        {
                            "entryId": "cursor-top-1722530761022",
                            "sortIndex": "1722530761022",
                            "content": {
                                "operation": {
                                    "cursor": {
                                        "value": "DAABDAABCgABFl7jfjmaYAAIAAIAAAABCAADiJONcggABBMoIV0ACwACAAAAC0FaRU8xWWs5dlFvAAA",
                                        "cursorType": "Top"
                                    }
                                }
                            }
                        },
                        {
                            "entryId": "cursor-bottom-1722530761020",
                            "sortIndex": "1722530761020",
                            "content": {
                                "operation": {
                                    "cursor": {
                                        "value": "DAACDAABCgABFl7jfjmaYAAIAAIAAAABCAADiJONcggABBMoIV0ACwACAAAAC0FaRU8xWWs5dlFvAAA",
                                        "cursorType": "Bottom"
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "clearEntriesUnreadState": {}
            },
            {
                "markEntriesUnreadGreaterThanSortIndex": {
                    "sortIndex": "1722530761021"
                }
            }
        ]
    }
}'''

data_dict = json.loads(data_list)

# print(data_dict)
print(data_dict['globalObjects'])


# json的序列化  python的代码转换成json的字符串             !!!注意json格式字符串一定是双引号，True是true，没有tuple而是list

new_dict = {'k1':123,'k2':True,'k3':(1,2,3,4,5)}        #{"k1": 123, "k2": true, "k3": [1, 2, 3, 4, 5]}
json_string = json.dumps(new_dict)
print(json_string)
print(type(json_string))

'''
Supports the following objects and types by default:

    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict              | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str               | string        |
    +-------------------+---------------+
    | int, float        | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+
    
'''
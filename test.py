import time
import os
import json


# print(os.listdir())
# print(time.time())
#
# localtime = time.localtime()
# print(localtime)
# print(time.strftime("%Y-%m-%d %H:%M:%S %c", time.localtime()))

# C:\Users\16209\Desktop

# f = open(r"C:\Users\16209\Desktop\1.txt", "r", encoding='utf8')
# #通过read读取文件全部内容
# data1 = f.read()
# print("read对应结果: {}".format(data1))
# f.close()

# f = open(r"C:\Users\16209\Desktop\1.txt", "r", encoding='utf8')
# #通过read读取一行内容
# data1 = f.readlines()
# print("read对应结果: {}".format(data1))
# f.close()

# f = open(r"C:\Users\16209\Desktop\1.txt", "w", encoding='utf8')
# data1 = f.write('第六行')
# print("read对应结果: {}".format(data1))
# f.close()

# with open(r"C:\Users\16209\Desktop\1.txt", "w", encoding='utf8') as f:
#     data = ['name1\n', 'age\n', 'sex\n']
#     f.writelines(data)

# dict1 = {"name": "storm", "age": 35}
# print(dict1)
# print(type(dict1))
#
# #将字典转化为字符串
# j1 = json.dumps(dict1)
# print(j1)
# print(type(j1))

# dict1 = {"name": "storm", "age": 35}
# print(dict1)
# print(type(dict1))
# #将字典写入txt文件
# with open(r"C:\Users\16209\Desktop\1.txt", "w", encoding='utf8') as f:
#     j1 = json.dump(dict1, f)
#     print(j1)
#     print(type(j1))

# file = r"C:\Users\16209\Desktop\2.json"
# with open(file, 'r') as f:
#     users = json.load(f)
#     print(type(f))
#     print(type(users))
#     print(users)
# for user in users:
#     print(user)
#     print(type(user))
#     name = users[user]['name']['pet']
#     print(name)
#     password = users[user]['password']
#     print(name, password)

# file = r"C:\Users\16209\Desktop\3.json"
# with open(file, 'r') as f:
#     ss = json.load(f)
#
# for s in ss:
#     print(s)
#     print(s["name"])
#     print(s["age"])

def parse_json(file, key1, key2):
    mylist = []
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
        for i in data:
            print(i)
            mylist.append((data[i][key1], data[i][key2]))
            return mylist


if __name__ == '__main__':
    account_info = parse_json(r"C:\Users\16209\Desktop\2.json"
                              , 'name', 'password')
    print(account_info)
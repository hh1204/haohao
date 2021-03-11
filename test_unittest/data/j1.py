import json

# 1、首先创建一个字典
data = {'name': 'haohao', 'age': None,'favor':True,'gender':False}
# 打印看类型
print(data)
print(type(data))
# 2、字典转换为json用dumps；这也就是序列化
# 处理中文字符问题， ensure_ascii 参数
data_json = json.dumps(data, ensure_ascii=False)
# 打印看转换后的类型
print(data_json)
print(type(data_json))

# json转化成字典用loads；这也就是反序列化
json_dict = json.loads(data_json)
# 打印看转换后的类型
print(json_dict)
print(type(json_dict))

# 为啥处理字符问题不用encoding='utf-8'而用ensure_ascii=False？我们打印看结果就知道了
# 字符串当中应该是用双引号，而不能用单引号
wrong_json = '{"name": "haohao"}'
print(json.loads(wrong_json, encoding='utf-8'))


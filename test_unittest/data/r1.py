# 导入Python自带的re模块
import re

"""re.match() 能够匹配出以xxx开头的字符串
    match()方法需要传两个参数，第一个参数是写的正则表达式，第二个参数是要匹配的字符串
"""
# result = re.match("haohao","haohao.com")
# # 如果能匹配到的话可以使用group方法来提取数据
# print(result.group())
#
# # .的使用
# ret1 = re.match(".","hao")
# print(ret1.group())
# # .的使用
# ret2 = re.match("h.o","hoo")
# print(ret2.group())
# # .的使用
# ret3 = re.match("h.o","hao")
# print(ret3.group())
#
# # 如果hello的首字符小写，那么正则表达式需要小写的h
# ret = re.match("h","hello Python")
# print(ret.group())
#
#
# # 如果hello的首字符大写，那么正则表达式需要大写的H
# ret = re.match("H","Hello Python")
# print(ret.group())
#
# # 大小写h都可以的情况，[]的使用
# ret = re.match("[hH]","hello Python")
# print(ret.group())
# ret = re.match("[hH]","Hello Python")
# print(ret.group())
# ret = re.match("[hH]ello Python","Hello Python")
# print(ret.group())
#
# # 匹配0到9第一种写法
# ret = re.match("[0123456789]Hello Python","7Hello Python")
# print(ret.group())
#
# # 匹配0到9第二种写法
# ret = re.match("[0-9]Hello Python","7Hello Python")
# print(ret.group())
#
# ret = re.match("[0-35-9]Hello Python","7Hello Python")
# print(ret.group())
#
# # 下面这个正则不能够匹配到数字4，因此ret为None
# ret = re.match("[0-35-9]Hello Python","4Hello Python")
# # print(ret.group())
#
# # 普通的匹配方式
# ret = re.match("浩浩1号","浩浩1号是我")
# print(ret.group())
#
# ret = re.match("浩浩2号","浩浩2号是我")
# print(ret.group())
#
# # 使用\d进行匹配
# ret = re.match("浩浩\d号","浩浩1号是我")
# print(ret.group())
#
# ret = re.match("浩浩\d号","浩浩2号是我")
# print(ret.group())

# 使用*进行匹配  需求：匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
# ret = re.match("[A-Z][a-z]*","H")
# print(ret.group())
#
# ret = re.match("[A-Z][a-z]*","HaoH")
# print(ret.group())
#
# names = ["name1", "_name", "2_name", "__name__"]
#
# # 使用+进行匹配 需求：匹配出，变量名是否有效
# for name in names:
#     ret = re.match("[a-zA-Z_]+[\w]*",name)
#     if ret:
#         print("变量名 %s 符合要求" % ret.group())
#     else:
#         print("变量名 %s 非法" % name)
# # 使用?进行匹配 需求：匹配出，0到99之间的数字
# ret = re.match("[1-9]?[0-9]","7")
# print(ret.group())
#
# ret = re.match("[1-9]?\d","33")
# print(ret.group())
#
# ret = re.match("[1-9]?\d","09")
# print(ret.group())
# # 0 # 这个结果并不是想要的，利用$才能解决
#
# # 使用{m}进行匹配 需求：匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
# ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
# print(ret.group())
#
# ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
# print(ret.group())

# # 使用$进行匹配 需求：匹配163.com的邮箱地址
# email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
#
# for email in email_list:
#     ret = re.match("[\w]{4,20}@163\.com", email)
#     if ret:
#         print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
#     else:
#         print("%s 不符合要求" % email)
#
# # 完善后
# email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
#
# for email in email_list:
#     ret = re.match("[\w]{4,20}@163\.com$", email)
#     if ret:
#         print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
#     else:
#         print("%s 不符合要求" % email)


# 使用|进行匹配 需求：匹配出0-100之间的数字
ret = re.match("[1-9]?\d","8")
print(ret.group())  # 8

ret = re.match("[1-9]?\d","78")
print(ret.group())  # 78

# 不正确的情况
ret = re.match("[1-9]?\d","08")
print(ret.group())  # 0

# 修正之后的
ret = re.match("[1-9]?\d$","08")
if ret:
    print(ret.group())
else:
    print("不在0-100之间")

# 添加|
ret = re.match("[1-9]?\d$|100","8")
print(ret.group())  # 8

ret = re.match("[1-9]?\d$|100","78")
print(ret.group())  # 78

ret = re.match("[1-9]?\d$|100","08")
# print(ret.group())  # 不是0-100之间

ret = re.match("[1-9]?\d$|100","100")
print(ret.group())  # 100

# 使用()进行匹配 需求：匹配出163、126、qq邮箱
ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())  # test@163.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())  # test@126.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())  # test@qq.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")  # 不是163、126、qq邮箱
# 不是以4、7结尾的手机号码(11位)

tels = ["13100001234", "18912344321", "10086", "18800007777"]

for tel in tels:
    ret = re.match("1\d{9}[0-35-68-9]", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的手机号" % tel)
# 提取区号和电话号码
ret = re.match("([^-]*)-(\d+)","010-12345678")
print(ret.group())
print(ret.group(1))
print(ret.group(2))

# 使用\进行匹配 需求：匹配出<html>hh</html>
# 能够完成对正确的字符串的匹配
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</html>")
print(ret.group())

# 如果遇到非正常的html格式字符串，匹配出错
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmlbalabala>")
print(ret.group())

# 正确的理解思路：如果在第一对<>中是什么，按理说在后面的那对<>中就应该是什么

# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())

# 因为2对<>中的数据不一致，所以没有匹配出来
test_label = "<html>hh</htmlbalabala>"
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", test_label)
if ret:
    print(ret.group())
else:
    print("%s 这是一对不正确的标签" % test_label)

# 使用\number进行匹配 需求：匹配出<html><h1>www.haohao.cn</h1></html>
labels = ["<html><h1>www.haohao.cn</h1></html>", "<html><h1>www.haohao.cn</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

# 使用(?P<name>) (?P=name)进行匹配 需求：匹配出<html><h1>www.haohao.cn</h1></html>
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.haohao.cn</h1></html>")
ret.group()

ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.haohao.cn</h2></html>")
ret.group()
# 注意：(?P<name>)和(?P=name)中的字母p大写
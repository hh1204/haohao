import logging

# 初始化logger，快速的完成配置，然后就可以用了
# 默认级别是WARNING，意思就是只有WARING和比WARNING更严重的问题才会被记录到日志内
# 注意 level如果后面直接跟值的话，值必须大写，否则报错
# logging.basicConfig(level='INFO')
# 第二种初始化方法，我们级别设置成debug
logging.basicConfig(level=logging.DEBUG)

# 如果我们不设置级别，默认就是warning
logging.basicConfig(filename='mylog.log',level=logging.DEBUG)


# 看一下源码，了解每个日志级别,注意是全部大写！因为它们是常量
# NOTSET = 0  如果出现这个级别就理解为你们领导和你们说的废话一样，不用听，不用管
logging.NOTSET
# DEBUG = 10  和主体功能无关，比如：某个功能的非必填项，如果填了会出现的问题
logging.debug("我是debug")
# INFO = 20    主要的功能信息，日志常用的错误级别
logging.info("我是info")
# WARNING = 30   警告  告诉你这块可能要要出问题了
logging.warning("我是warning")
# ERROR = 40     次严重问题的错误，比如：分支流程不通
logging.error("我是error")
# CRITICAL = 50    最严重的的问题，比如系统主流程不通
logging.critical("我是critical")





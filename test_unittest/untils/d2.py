import logging

# 1、创建日志收集器，收集log信息的
log_shouji = logging.getLogger("浩浩的日志")
# 2、设置日志收集器的级别
log_shouji.setLevel(logging.DEBUG)

# 3、日志处理器
# 哪里显示我们的日志信息
# 控制台显示
concole_handler = logging.StreamHandler()
# 初始化文件显示
file_handler = logging.FileHandler("mylog.log",encoding='utf-8')

# 4、处理器级别设置
concole_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# 5、把日志处理器添加到日志收集器里面
log_shouji.addHandler(concole_handler)
log_shouji.addHandler(file_handler)

# 6、初始化格式器
concole_fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# 7、设置处理器的格式
concole_handler.setFormatter(concole_fmt)

file_fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
file_handler.setFormatter(file_fmt)

log_shouji.debug("浩浩在上班")
log_shouji.info("浩浩明天还要上班")
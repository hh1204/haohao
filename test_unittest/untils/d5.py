import logging
import os
from logging import handlers

# 项目绝对路径
path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name,
                 level=0,
                 file_name="{}/logs/all.log".format(path),
                 handler_level=0,
                 fmt="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                 when='S',
                 backupCount=3,
                 encoding='utf-8',
                 **kw
                 ):
        """初始化函数。完成 level, format, handler 配置"""
        # 子类的初始化使用了父类的
        super().__init__(name, level=level)

        # 初始化 handler
        if not file_name:
            handler = logging.StreamHandler()
        else:
            # 往文件里写入,指定间隔时间自动生成文件的处理器
            handler = handlers.TimedRotatingFileHandler(filename=file_name,
                                                        when=when,
                                                        backupCount=backupCount,
                                                        encoding=encoding)
            # 实例化TimedRotatingFileHandler
            # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时
            # D 天
            # W{0-6} 星期几（interval=0时代表星期一）
            # midnight 每天凌晨
            # 设置handler日志的级别
        handler.setLevel(handler_level)
        # 添加handler
        self.addHandler(handler)
        # 设置format
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)


logger = LoggerHandler("浩浩")

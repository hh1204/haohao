from configparser import ConfigParser

conf = ConfigParser()
conf.read('./setting.ini',encoding='utf-8')

print(conf.get('logger','name'))

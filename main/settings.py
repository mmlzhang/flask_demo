
import os

import pymongo
import redis


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件目录
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# mongodb 设置
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PASSWORD = ''

conn = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
MONGO_DATABASE = conn.renrenche  # 连接的数据库

# MySQL数据库配置
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'rrc'  # 数据库名称
MYSQL_USER = 'root'  # 用户名
MYSQL_PASSWORD = '123456'  # 用户密码

MYSQL_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(
    host = MYSQL_HOST,
    port = MYSQL_PORT,
    database = MYSQL_DATABASE,
    user = MYSQL_USER,
    password = MYSQL_PASSWORD,
)

# redis 初始化配置
REDIS_HOST = '127.0.0.1'  # ip
REDIS_PORT = 6379  # 端口
REDIS_USER = ''  # 用户
REDIS_PASSWORD = ''  #密码

# 连接redis
REDIS_CONN = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

# session 安全密钥
SECRET_KEY = 'jdsklfjo678*……*5645435njh*NBGF(kv%&^%&$%JK'

# 配置
MAIN_CONFIG = {
    'SQLALCHEMY_DATABASE_URI': MYSQL_URI,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SESSION_TYPE': 'redis',  # session种类
    'SECRET_KEY': SECRET_KEY,
    'SESSION_REDIS': REDIS_CONN,
    'SESSION_KEY_PREFIX': os.path.split(BASE_DIR)[-1],  # 这里是你的项目的名称
}

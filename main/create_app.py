
from flask import Flask

from app.user_views import user_blueprint
from .settings import MAIN_CONFIG, STATIC_DIR, TEMPLATES_DIR, start_logging
from .ext_init import ext_init


def create_app():
    """ 创建app,注册配置 """
    # 开始记录日志
    start_logging()
    # 初始化 app
    app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATES_DIR)
    # 注册路由
    app.register_blueprint(blueprint=user_blueprint,
                           url_prefix='/user')
    # 增加配置文件
    app.config.update(MAIN_CONFIG)
    ext_init(app=app)
    return app
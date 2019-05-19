
"""注册要初始化的app"""

from flask_session import Session


se = Session()
db = ''


def ext_init(app):
    se.init_app(app=app)
    # db.init_app(app=app)
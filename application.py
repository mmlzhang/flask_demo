
from flask_script import Manager

from demo_code.main import create_app


app = create_app()
manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
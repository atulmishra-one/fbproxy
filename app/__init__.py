from app.instance import create_app
from app.config import app_config
import os

application = create_app(app_config[os.getenv('APP_CONFIG')])
application.app_context().push()

if __name__ == '__main__':
    application.run()


#run

import os

from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name = "production")

if __name__ == '__main__':
    app.run()
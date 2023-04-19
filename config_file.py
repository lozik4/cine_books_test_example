import os

ENV_PARAM = os.environ.get('ENV', 'PROD')

if ENV_PARAM == 'DEV':
    print(ENV_PARAM)
    from configs.dev import *
elif ENV_PARAM == 'STAGE':
    print(ENV_PARAM)
    from configs.stage import *
elif ENV_PARAM == 'PROD':
    print(ENV_PARAM)
    from configs.prod import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALLURE_RESULTS_DIR = BASE_DIR + '/allure-results'

HUB = 'http://localhost:4444'

SCREEN_HEIGHT: int = 768  # need min design screen height
SCREEN_WIDTH: int = 1440   # need min design screen width

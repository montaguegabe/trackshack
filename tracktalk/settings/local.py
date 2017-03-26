import environ

environ.Env.read_env('.env')

from .common import *

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

# Static serving
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATIC_URL = '/static/'

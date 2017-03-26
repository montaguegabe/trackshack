from .common import *

DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

# AWS shared settings
# Use this to control the cache time of the files once things have settled
"""AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
}"""


# Static files
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static_collected')
STATIC_ROOT = join(PUBLIC_DIR, 'static')
STATICFILES_LOCATION = 'static'

AWS_STORAGE_BUCKET_NAME = env('AWS_BUCKET_NAME') #'parkandpedal-content'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_ACCESS_KEY_SECRET')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATIC_URL = AWS_STATIC_URL

# Feed static files to AWS Boto backend
STATICFILES_STORAGE = 'custom_storages.StaticStorage'


# Media files
MEDIA_ROOT = join(PUBLIC_DIR, 'media')
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

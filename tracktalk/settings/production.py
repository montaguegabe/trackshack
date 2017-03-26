from .common import *

DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com', '.trackshack.org']

# AWS shared settings
# Use this to control the cache time of the files once things have settled
"""AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
}"""


# Static files
STATICFILES_LOCATION = 'static'

AWS_STORAGE_BUCKET_NAME = env('AWS_BUCKET_NAME') #'parkandpedal-content'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_ACCESS_KEY_SECRET')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Feed static files to AWS Boto backend
STATICFILES_STORAGE = 'custom_storages.StaticStorage'


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# Security

# Only send the CSRF cookie over HTTPS
CSRF_COOKIE_SECURE = True

# Disallow JS from getting the CSRF token cookie
CSRF_COOKIE_HTTPONLY = False

# Only send the session data over HTTPS
SESSION_COOKIE_SECURE = True

# How long for the browser to wait before non-https requests are accepted
#SECURE_HSTS_SECONDS = 0

# Instructs the browser to always trust the server-dictated content types
#SECURE_CONTENT_TYPE_NOSNIFF = True

# Instructs the browser to try to block XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Redirect any HTTP connection to HTTPS
SECURE_SSL_REDIRECT = True

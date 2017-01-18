import os

"""
Main Settings
"""
DEBUG = False
ALLOWED_HOSTS = ['.adv.bvodola.webfactional.com', '.adv.mpg.net.br']
ADMINS = (('Brunno', 'bvodola@gmail.com'),)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Database
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'adv_db',
        'USER': 'bvodola',
        'PASSWORD': 'qZwX1001'
    }
}

"""
Static files
"""
STATIC_ROOT = '/home/bvodola/webapps/adv_static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
E-mail settings
"""
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'mpg_mail'
EMAIL_HOST_PASSWORD = 'qZwX1001'
DEFAULT_FROM_EMAIL = 'contato@mpg.net.br'
SERVER_EMAIL = 'contato@mpg.net.br'

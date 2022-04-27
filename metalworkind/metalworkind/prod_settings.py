import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'metalworkind.com', 'www.metalworkind.com','192.168.88.101', '192.168.88.104',]

# STATICFILES_DIRS = ['/usr/local/lib/python3.8/site-packages/django/contrib/admin/static']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
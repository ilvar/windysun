import os
import sys
import django.core.handlers.wsgi

sys.path.append('/var/www/')
sys.path.append('/var/www')
sys.path.append('/var/www/windyeng/')
sys.path.append('/var/www/windyeng')


os.environ['DJANGO_SETTINGS_MODULE'] = 'windyeng.settings'
application = django.core.handlers.wsgi.WSGIHandler()

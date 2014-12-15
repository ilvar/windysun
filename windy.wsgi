import os
import sys
import django.core.handlers.wsgi

sys.path.append('/var/www/')
sys.path.append('/var/www')
sys.path.append('/var/www/windy/')
sys.path.append('/var/www/windy')


os.environ['DJANGO_SETTINGS_MODULE'] = 'windy.settings'
application = django.core.handlers.wsgi.WSGIHandler()

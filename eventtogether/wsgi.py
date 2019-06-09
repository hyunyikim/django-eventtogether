"""
WSGI config for eventtogether project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# settings 모듈의 위치를 지정함
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventtogether.settings")

application = get_wsgi_application()

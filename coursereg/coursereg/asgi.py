"""
ASGI config for coursereg project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coursereg.settings")

application = get_asgi_application()

import os
from importlib import import_module


def import_module_attr(path):
    package, module = path.rsplit('.', 1)
    return getattr(import_module(package), module)

settings = import_module_attr(
    os.getenv('COMMENTS_MODERATION_SETTINGS_MODULE', 'django.conf.settings')
)

MODERATION_MODE = getattr(settings, 'COMMENTS_MODERATION_MODE', 'approve')

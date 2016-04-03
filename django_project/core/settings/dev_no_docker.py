# coding=utf-8
import os
from .dev import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'qgis_sharing_platform',
    }
}

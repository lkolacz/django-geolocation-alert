# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


GEOLOCATION_IS_ACTIVE = getattr(settings, 'GEOLOCATION_IS_ACTIVE', True)

GEOLOCATION_HASH = getattr(settings, 'GEOLOCATION_HASH', 'geolocation_hash')

GEOLOCATION_SEND_SIGNAL = getattr(settings, 'GEOLOCATION_SEND_SIGNAL', False)
GEOLOCATION_SEND_MSG = getattr(settings, 'GEOLOCATION_SEND_MSG', None)

if GEOLOCATION_SEND_MSG is None:
    GEOLOCATION_SEND_MSG = _(
        "IP address or agent browser change during session time,"
        " after log on.")

GEOLOCATION_USER_MODELS = getattr(settings, 'GEOLOCATION_USER_MODELS', None)

GEOLOCATION_STAFF_REDIRECT = \
    getattr(settings, 'GEOLOCATION_STAFF_REDIRECT', False)
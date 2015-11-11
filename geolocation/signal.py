# -*- coding: utf-8 -*-
from django.dispatch import Signal
from django.contrib.auth.signals import user_logged_in

from .settings import GEOLOCATION_HASH
from .utils import get_user, get_user_session_geolocation_hash

geolocation_signal = Signal(providing_args=["request", "user"])


class GeolocationAlert(object):

    def send_alert_signal(self, request, user):
        geolocation_signal.send(
            sender=self.__class__, reques=request, user=user)


def add_hash_geolocation(sender, user, request, **kwargs):
    """
    Hash geolocation set up on login signal to perform alert.
    """
    if get_user(request) is not None:
        request.session[GEOLOCATION_HASH] = \
            get_user_session_geolocation_hash(request)
        request.session.modified = True
user_logged_in.connect(add_hash_geolocation)

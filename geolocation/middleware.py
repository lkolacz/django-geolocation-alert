# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, HttpResponse

from .utils import get_user, get_user_session_geolocation_hash
from .signal import GeolocationAlert
from .settings import (
    GEOLOCATION_IS_ACTIVE,
    GEOLOCATION_HASH,
    GEOLOCATION_SEND_SIGNAL,
    GEOLOCATION_SEND_MSG,
    GEOLOCATION_STAFF_REDIRECT,
)


class GeolocationMiddleware(object):

    def process_response(self, request, response):
        """
        Geolocation middleware processing.
        If session hash (contained IP and agent browser name) will change
        during session time GWM will redirect to logout page and send
        "geolocation_watchman.signal.geolocation_watchman_signal"
        """
        if not GEOLOCATION_IS_ACTIVE:
            return response or HttpResponse(request)

        user = get_user(request)
        if user:
            expected_hash = request.session.get(GEOLOCATION_HASH)
            hash_to_check = get_user_session_geolocation_hash(request)
            if expected_hash and hash_to_check != expected_hash:
                logout_url = settings.LOGOUT_URL
                if GEOLOCATION_STAFF_REDIRECT and\
                        getattr(user, 'is_staff', False):
                    logout_url = 'admin:logout'
                response = redirect(logout_url)
                if GEOLOCATION_SEND_MSG:
                    messages.add_message(
                        request,
                        messages.WARNING,
                        GEOLOCATION_SEND_MSG
                    )
                if GEOLOCATION_SEND_SIGNAL:
                    alert = GeolocationAlert()
                    alert.send_alert_signal(request, user)

        return response or HttpResponse(request)

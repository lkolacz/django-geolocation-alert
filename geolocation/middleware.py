# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout

from .utils import get_user, get_user_session_geolocation_hash
from .signal import GeolocationAlert
from .settings import (
    GEOLOCATION_IS_ACTIVE,
    GEOLOCATION_HASH,
    GEOLOCATION_SEND_SIGNAL,
    GEOLOCATION_SEND_MSG,
)


class GeolocationMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Geolocation middleware processing.
        If session hash (contained IP and agent browser name) will change
        during session time GWM will redirect to logout page and send
        "geolocation.signal.geo_alert_occurred" signal.
        """
        if not GEOLOCATION_IS_ACTIVE:
            return

        user = get_user(request)
        if user:
            expected_hash = request.session.get(GEOLOCATION_HASH)
            hash_to_check = get_user_session_geolocation_hash(request)
            if expected_hash and hash_to_check != expected_hash:
                logout(request)
                if GEOLOCATION_SEND_MSG:
                    messages.add_message(
                        request,
                        messages.WARNING,
                        GEOLOCATION_SEND_MSG
                    )
                if GEOLOCATION_SEND_SIGNAL:
                    alert = GeolocationAlert()
                    alert.send_alert_signal(request, user)


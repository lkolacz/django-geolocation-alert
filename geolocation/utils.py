# -*- coding: utf-8 -*-
import base64

from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.utils import six

from .settings import GEOLOCATION_USER_MODELS


__use_forwarded = getattr(settings, 'USE_X_FORWARDED_HOST', False)


def __get_model(relation):
    if isinstance(relation, six.string_types):
        try:
            app_label, model_name = relation.split(".")
            return apps.get_model(app_label=app_label, model_name=model_name)
        except ValueError:
            pass
    raise ImproperlyConfigured(
        "Defined relation should contain app_label.model_name"
        " string construction. Was (%s)." % relation)


__user_classes = []

if isinstance(GEOLOCATION_USER_MODELS, list):
    for relation in GEOLOCATION_USER_MODELS:
        __user_classes.append(__get_model(relation))
else:
    __user_classes.append(get_user_model())

__user_classes = tuple(__user_classes)


def get_user(request):
    """
    Function that get user from request if user is an instance of
    AUTH_USER_MODEL by default or check user instance by given list of
    user model by like:
    >>> GEOLOCATION_USER_MODELS = ["auth.User", "panel.UserPanel"]

    @param request: django request
    @rtype: get_user_model() or None
    """
    global __user_classes
    user = getattr(request, 'user', None)
    if isinstance(user, __user_classes):
        return user
    else:
        return None


def __get_remote_addr(request):
    """
    Getting IP address from request META headers.
    """
    global __use_forwarded
    addr = None
    if __use_forwarded:
        addr = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if addr is None:
        addr = request.META.get('REMOTE_ADDR', None)
    return addr


def get_user_session_geolocation_hash(request=None, agent='', addr=''):
    """
    Function generate hash by given address IP and HTTP User Agent.
    If USE_X_FORWARDED_HOST setting is set to True then
    HTTP_X_FORWARDED_FOR header is taken from request.META instead of
    REMOTE_ADDR header.

    @param request: django.http.HttpRequest
    @param agent: string (browser agent name)
    @param addr: string (IP user address)
    @rtype: string (hash)
    """
    if request:
        agent = request.META.get('HTTP_USER_AGENT')
        addr = __get_remote_addr(request)

    if not agent or not addr:
        return None

    value = addr + "||" + agent
    return base64.b64encode(value)

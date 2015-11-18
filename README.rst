Django Geolocation Alert
========================

Django Geolocation Alert is an middleware that control user IP address
and agent browser during session time. If someone will take session id 
and try to use it from another IP or different agent browser Alert will raise
so user will be logged out with alert messages.
You can also turn on send signal to make some custom staff by handling it.
Lot of User class that can be authenticated? Don't worry take a look below.

The app integrates smoothly with any Django project.
All You need to do is install app and add middleware to MIDDLEWARE_CLASSES
in settings. Please read Quick start to know hot to do that.


Features
--------

* Set geolocation user hash to request.session when user_logged_in signal is send
* Define User model(s) class that geolocation alert should raise
* Send geolocation alert as signal if User IP or agent browser will change and logout
* Override settings if needed

Future Features
---------------

* Confirm it works on django 1.7
* PY2 & PY3 compabilities
* Django downgrade compabilities 1.6, 1.5, 1.4
* unit tests

Requirements
------------

* Django == 1.8
* Python == 2.7

License
-------

MIT

Quick Start
-----------

Install django-geolocation-alert in your system by command::

    pip install django-geolocation-alert

Then use it in a django project by putting middleware to Your settings::

    MIDDLEWARE_CLASSES = (
        ..
        'geolocation.middleware.GeolocationMiddleware'
    )

Now it's works :)

More custom? Ok, lets handle alert signals!

1. Make some function::

    def alert_geolocation_handler(sender, request, user, **kwargs):
        # do some staff
        # deactivate User and force SMS code send to confirm identity
        ..

2. Connect Your function with signal::

    from geolocation.signal import geo_alert_occurred
    geo_alert_occurred.connect(alert_geolocation_handler)
    # I suggest connect it inside "basic app_module.views.py"
    # make sure that geo_alert_occurred.has_listeners() is True

3. Last step -> Turn On send alert signal in your prj settings::

    GEOLOCATION_SEND_SIGNAL = True


django.conf.settings
--------------------

Override some of them if needed.


**GEOLOCATION_HASH**

Default session key name that storage geolocation hash is 'geolocation_hash'.
If for any reason You want it to change, go straight ahead.

**GEOLOCATION_SEND_SIGNAL**

Default is set to False, but if you need to do some staff with this event
just turn it on and make some handler for your purpose.

**GEOLOCATION_SEND_MSG**

Default is set to None. This will add standard messages (django.contrib.messages)
as an messages.WARNING mode with text::

    IP address or agent browser change during session time, after log on.

If You want set different message just set it in prj settings::

    from django.utils.translation import ugettext_lazy as _
    GEOLOCATION_SEND_MSG = _('You bastard!!! I got you!!!')

Or turn it off by::

    GEOLOCATION_SEND_MSG = False

**GEOLOCATION_USER_MODELS**

Default is None. Please change it if You have many users model classes which You
want to be handle by geolocation alert::

    GEOLOCATION_USER_MODELS = [
        "auth.User",
        "panel.PanelUser",
        "merchant.MerchantUser",
        "buyer.BuyerUser",
        "account.GuestAccount",
    ]

Now if anybody will take session id and will try it from different IP
or agent browser will be logged out. If there is different User class,
not noticed in the list it won't be handled by alert!

**GEOLOCATION_IS_ACTIVE**

Default is set to True, but if You need to work on staging - for example,
with one admin for many users (testers and developers)
it's useful to turn it off.

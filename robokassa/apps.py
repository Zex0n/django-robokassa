# -*- encoding: utf-8 -*-
import django
if django.VERSION[0] > 3:
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class DBMailConfig(AppConfig):
    name = 'robokassa'
    verbose_name = _(u'Робокасса')

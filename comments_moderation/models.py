# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class EmailFilter(models.Model):
    email  = models.EmailField(verbose_name=_(u"Email"), null=True)
    active = models.BooleanField(help_text=_(u"Rule is active"))

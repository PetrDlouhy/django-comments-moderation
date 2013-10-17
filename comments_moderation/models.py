# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class EmailFilter(models.Model):
    RULE_CHOICES = (
            ('moderate', _(u'Moderate all comments')),
            ('approve', _(u'Approve all comments')),
            ('new', _(u'New user')),
        )

    email  = models.EmailField(
            verbose_name=_(u"Email"),
            null=True
            )
    active = models.CharField(
            max_length = 20,
            help_text=_(u"Mode of moderation"),
            choices=RULE_CHOICES, default = 'new'
            )

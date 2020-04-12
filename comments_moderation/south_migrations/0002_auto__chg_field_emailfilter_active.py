# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EmailFilter.active'
        db.alter_column(u'comments_moderation_emailfilter', 'active', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'EmailFilter.active'
        db.alter_column(u'comments_moderation_emailfilter', 'active', self.gf('django.db.models.fields.BooleanField')())

    models = {
        u'comments_moderation.emailfilter': {
            'Meta': {'object_name': 'EmailFilter'},
            'active': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['comments_moderation']
from comments_moderation.models import EmailFilter
from django.contrib import admin

class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('email', 'active')

admin.site.register(EmailFilter, BlacklistAdmin)

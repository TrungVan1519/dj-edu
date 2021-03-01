from django.contrib import admin

from .models import ShortenedUrl

admin.AdminSite.site_header = 'Django Edu Admin Site'
admin.AdminSite.site_title = 'Admin Area'
admin.AdminSite.index_title = 'Welcome, admin'


class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'link', 'date_created')
    empty_value_display = '-None-'


admin.site.register(ShortenedUrl, ShortenedUrlAdmin)

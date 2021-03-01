from django.contrib import admin

from .models import Word

admin.AdminSite.site_header = 'Django Edu Admin Site'
admin.AdminSite.site_title = 'Admin Area'
admin.AdminSite.index_title = 'Welcome, admin'


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword', 'meaning',
                    'synonym', 'antonym', 'date_created')
    empty_value_display = '-None-'


admin.site.register(Word, WordAdmin)

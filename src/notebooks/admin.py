from django.contrib import admin

from .models import Note

admin.AdminSite.site_header = 'Django Edu Admin Site'
admin.AdminSite.site_title = 'Admin Area'
admin.AdminSite.index_title = 'Welcome, admin'


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date_created', 'date_updated')
    empty_value_display = '-None-'


admin.site.register(Note, NoteAdmin)

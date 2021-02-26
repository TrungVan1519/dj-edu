from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date_created', 'date_updated')
    empty_value_display = '-None-'


admin.site.register(Note, NoteAdmin)

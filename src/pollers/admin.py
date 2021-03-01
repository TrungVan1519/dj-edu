from django.contrib import admin

from .models import Question, Choice

admin.AdminSite.site_header = 'Django Edu Admin Site'
admin.AdminSite.site_title = 'Admin Area'
admin.AdminSite.index_title = 'Welcome, admin'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_created', 'date_updated')
    fieldsets = (
        (None, {'fields': ['text']}),
        ('Date Created', {'fields': [
         'date_created'], 'classes': ('collapse')}),
        ('Date Updated', {'fields': [
         'date_updated'], 'classes': ('collapse')}),
    )
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'votes',
                    'date_created', 'date_updated')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

from django.contrib import admin

from .models import Question, Choice


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

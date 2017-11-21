from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Choice, Question


# this will change the order of the feilds that are displayed in the admin panel
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# this will put a bar on top of the admin panel

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date')
    # all of these things are what we want to activate in from the admin app / lib
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)

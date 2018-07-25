from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.AppUsers)
class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'Username', 'email', 'password',
    ]

@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_text', ]

@admin.register(models.Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ['Username','question_text','answer_text','score', ]
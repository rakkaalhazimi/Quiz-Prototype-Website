from django.contrib import admin

from .models import Questions, Answers

# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("question_number", "question")
    ordering = ["question_number"]

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers)